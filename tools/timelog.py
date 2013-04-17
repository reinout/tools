"""
This is a gtimelog variant/hack for the commandline.

`gtimelog <http://mg.pov.lt/gtimelog/>`_ requires gtk, which isn't handy on
OSX. Years ago I already hacked up a modified version that only requires the
commandline. I've dug it up again.

gtimelog is (c) Marius Gedminas, GPL. My stuff is GPL'ed too, so that fits :-)

My variant works on the commandline and provides two commands:

tl
    Add a timelog entry to the logfile. The entry to add is passed on the
    commandline, for instance ``tl weblog`` for when I worked on a blog
    entry.

    The logfile is ``~/.gtimelog/timelog.txt``.

pt
    Short for "print today", it prints an overview of how much time I spend on
    what today. Call it like ``pt week`` to get an overview of the whole week
    (and a couple of earlier weeks, in case I need that).

The ``tl`` command works best when you add tab completion. Add a
``~/.gtimelog/tasks.txt`` file, which should have one word per line, each
being a task you want to log with ``tl``. Hook up the following into your bash completion::

    _timelog()
    {
        local cur prev
        COMMAND_NAME='timelog'
        COMPREPLY=()
        # Word that is currently being expanded:
        cur=${COMP_WORDS[COMP_CWORD]}
        # Previous expanded word:
        prev=${COMP_WORDS[COMP_CWORD-1]}

        # We look for ~/.gtimelog/tasks.txt, which should have one word
        # per line, each being a project.
        CONFIGDIR=~/.gtimelog
        if test ! -d $CONFIGDIR; then
            return 0
        fi
        PROJECTS="$(cat $CONFIGDIR/tasks.txt | grep -v \#)"
        COMPREPLY=( $(compgen -W '$PROJECTS' -- $cur ) )
    }
    complete -F _timelog tl

Works quite well!

"""
import calendar
import csv
import datetime
import os
import re
import sys
import time

FILENAME = os.path.expanduser('~/.gtimelog/timelog.txt')
VIRTUAL_MIDNIGHT = datetime.time(5, 0)


# Note: add_timelog_entry() is hooked up as the 'tl' script.
# main() is hooked up as 'pt' ("print today").


def add_timelog_entry():
    """Main script to add an entry."""
    args = sys.argv[1:]
    if args[0].endswith('_'):
        first_argument = args[0]
        first_argument = first_argument[:-1]
        first_argument += '**'
        args[0] = first_argument
    entry = ' '.join(args)

    now = time.strftime('%Y-%m-%d %H:%M')
    line = '%s: %s' % (now, entry)
    try:
        f = open(FILENAME, "a")
    except IOError:
        f = open(FILENAME, "w")
    print line
    print >> f, line
    f.close()


def as_minutes(duration):
    """Convert a datetime.timedelta to an integer number of minutes."""
    return duration.days * 24 * 60 + duration.seconds // 60


def format_duration(duration):
    """Format a datetime.timedelta with minute precision."""
    h, m = divmod(as_minutes(duration), 60)
    return '%d h %d min' % (h, m)


def format_duration_short(duration):
    """Format a datetime.timedelta with minute precision."""
    h, m = divmod((duration.days * 24 * 60 + duration.seconds // 60), 60)
    return '%d:%02d' % (h, m)


def format_duration_long(duration):
    """Format a datetime.timedelta with minute precision, long format."""
    h, m = divmod((duration.days * 24 * 60 + duration.seconds // 60), 60)
    if h and m:
        return '%d hour%s %d min' % (h, h != 1 and "s" or "", m)
    elif h:
        return '%d hour%s' % (h, h != 1 and "s" or "")
    else:
        return '%d min' % m


def parse_datetime(dt):
    """Parse a datetime instance from 'YYYY-MM-DD HH:MM' formatted string."""
    m = re.match(r'^(\d+)-(\d+)-(\d+) (\d+):(\d+)$', dt)
    if not m:
        raise ValueError('bad date time: ', dt)
    year, month, day, hour, min = map(int, m.groups())
    return datetime.datetime(year, month, day, hour, min)


def parse_time(t):
    """Parse a time instance from 'HH:MM' formatted string."""
    m = re.match(r'^(\d+):(\d+)$', t)
    if not m:
        raise ValueError('bad time: ', t)
    hour, min = map(int, m.groups())
    return datetime.time(hour, min)


def virtual_day(dt, virtual_midnight):
    """Return the "virtual day" of a timestamp.

    Timestamps between midnight and "virtual midnight" (e.g. 2 am) are
    assigned to the previous "virtual day".
    """
    if dt.time() < virtual_midnight:     # assign to previous day
        return dt.date() - datetime.timedelta(1)
    return dt.date()


def different_days(dt1, dt2, virtual_midnight):
    """Check whether dt1 and dt2 are on different "virtual days".

    See virtual_day().
    """
    return virtual_day(dt1, virtual_midnight) != virtual_day(dt2,
                                                             virtual_midnight)


def uniq(l):
    """Return list with consecutive duplicates removed."""
    result = l[:1]
    for item in l[1:]:
        if item != result[-1]:
            result.append(item)
    return result


class TimeWindow(object):
    """A window into a time log.

    Reads a time log file and remembers all events that took place between
    min_timestamp and max_timestamp.  Includes events that took place at
    min_timestamp, but excludes events that took place at max_timestamp.

    self.items is a list of (timestamp, event_title) tuples.

    Time intervals between events within the time window form entries that have
    a start time, a stop time, and a duration.  Entry title is the title of the
    event that occurred at the stop time.

    The first event also creates a special "arrival" entry of zero duration.

    Entries that span virtual midnight boundaries are also converted to
    "arrival" entries at their end point.

    The earliest_timestamp attribute contains the first (which should be the
    oldest) timestamp in the file.
    """

    def __init__(self, filename, min_timestamp, max_timestamp,
                 virtual_midnight, callback=None):
        self.filename = filename
        self.min_timestamp = min_timestamp
        self.max_timestamp = max_timestamp
        self.virtual_midnight = virtual_midnight
        self.reread(callback)

    def reread(self, callback=None):
        """Parse the time log file and update self.items.

        Also updates self.earliest_timestamp.
        """
        self.items = []
        self.earliest_timestamp = None
        try:
            f = open(self.filename)
        except IOError:
            return
        line = ''
        for line in f:
            if ': ' not in line:
                continue
            time, entry = line.split(': ', 1)
            try:
                time = parse_datetime(time)
            except ValueError:
                continue
            else:
                entry = entry.strip()
                if callback:
                    callback(entry)
                if self.earliest_timestamp is None:
                    self.earliest_timestamp = time
                if self.min_timestamp <= time < self.max_timestamp:
                    self.items.append((time, entry))
        f.close()

    def last_time(self):
        """Return the time of the last event (or None if there are no events).
        """
        if not self.items:
            return None
        return self.items[-1][0]

    def all_entries(self):
        """Iterate over all entries.

        Yields (start, stop, duration, entry) tuples.  The first entry
        has a duration of 0.
        """
        stop = None
        for item in self.items:
            start = stop
            stop = item[0]
            entry = item[1]
            if start is None or different_days(start, stop,
                                               self.virtual_midnight):
                start = stop
            duration = stop - start
            yield start, stop, duration, entry

    def count_days(self):
        """Count days that have entries."""
        count = 0
        last = None
        for start, stop, duration, entry in self.all_entries():
            if last is None or different_days(last, start,
                                              self.virtual_midnight):
                last = start
                count += 1
        return count

    def last_entry(self):
        """Return the last entry (or None if there are no events).

        It is always true that

            self.last_entry() == list(self.all_entries())[-1]

        """
        if not self.items:
            return None
        stop = self.items[-1][0]
        entry = self.items[-1][1]
        if len(self.items) == 1:
            start = stop
        else:
            start = self.items[-2][0]
        if different_days(start, stop, self.virtual_midnight):
            start = stop
        duration = stop - start
        return start, stop, duration, entry

    def grouped_entries(self, skip_first=True):
        """Return consolidated entries (grouped by entry title).

        Returns two list: work entries and slacking entries.  Slacking
        entries are identified by finding two asterisks in the title.
        Entry lists are sorted, and contain (start, entry, duration) tuples.
        """
        work = {}
        slack = {}
        for start, stop, duration, entry in self.all_entries():
            if skip_first:
                skip_first = False
                continue
            if '**' in entry:
                entries = slack
            else:
                entries = work
            if entry in entries:
                old_start, old_entry, old_duration = entries[entry]
                start = min(start, old_start)
                duration += old_duration
            entries[entry] = (start, entry, duration)
        work = work.values()
        work.sort()
        slack = slack.values()
        slack.sort()
        return work, slack

    def totals(self):
        """Calculate total time of work and slacking entries.

        Returns (total_work, total_slacking) tuple.

        Slacking entries are identified by finding two asterisks in the title.

        Assuming that

            total_work, total_slacking = self.totals()
            work, slacking = self.grouped_entries()

        It is always true that

            total_work = sum([duration for start, entry, duration in work])
            total_slacking = sum([duration
                                  for start, entry, duration in slacking])

        (that is, it would be true if sum could operate on timedeltas).
        """
        total_work = total_slacking = datetime.timedelta(0)
        for start, stop, duration, entry in self.all_entries():
            if '**' in entry:
                total_slacking += duration
            else:
                total_work += duration
        return total_work, total_slacking

    def icalendar(self, output):
        """Create an iCalendar file with activities."""
        print >> output, "BEGIN:VCALENDAR"
        print >> output, "PRODID:-//mg.pov.lt/NONSGML GTimeLog//EN"
        print >> output, "VERSION:2.0"
        try:
            import socket
            idhost = socket.getfqdn()
        except:  # can it actually ever fail?
            idhost = 'localhost'
        dtstamp = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
        for start, stop, duration, entry in self.all_entries():
            print >> output, "BEGIN:VEVENT"
            print >> output, "UID:%s@%s" % (hash((start, stop, entry)), idhost)
            print >> output, "SUMMARY:%s" % (entry.replace('\\', '\\\\')
                                                  .replace(';', '\\;')
                                                  .replace(',', '\\,'))
            print >> output, "DTSTART:%s" % start.strftime('%Y%m%dT%H%M%S')
            print >> output, "DTEND:%s" % stop.strftime('%Y%m%dT%H%M%S')
            print >> output, "DTSTAMP:%s" % dtstamp
            print >> output, "END:VEVENT"
        print >> output, "END:VCALENDAR"

    def to_csv(self, output, title_row=True):
        """Export work entries to a CSV file.

        The file has two columns: task title and time (in minutes).
        """
        writer = csv.writer(output)
        if title_row:
            writer.writerow(["task", "time (minutes)"])
        work, slack = self.grouped_entries()
        work = [(entry, as_minutes(duration))
                for start, entry, duration in work
                if duration]  # skip empty "arrival" entries
        work.sort()
        writer.writerows(work)

    def daily_report(self, output, email, who):
        """Format a daily report.

        Writes a daily report template in RFC-822 format to output.
        """
        # Locale is set as a side effect of 'import gtk', so strftime('%a')
        # would give us translated names
        weekday_names = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        weekday = weekday_names[self.min_timestamp.weekday()]
        week = self.min_timestamp.strftime('%V')
        print >> output, "To: %(email)s" % {'email': email}
        print >> output, ("Subject: %(date)s report for %(who)s"
                          " (%(weekday)s, week %(week)s)"
                          % {'date': self.min_timestamp.strftime('%Y-%m-%d'),
                             'weekday': weekday, 'week': week, 'who': who})
        print >> output
        items = list(self.all_entries())
        if not items:
            print >> output, "No work done today."
            return
        start, stop, duration, entry = items[0]
        entry = entry[:1].upper() + entry[1:]
        print >> output, "%s at %s" % (entry, start.strftime('%H:%M'))
        print >> output
        work, slack = self.grouped_entries()
        total_work, total_slacking = self.totals()
        if work:
            for start, entry, duration in work:
                entry = entry[:1].upper() + entry[1:]
                print >> output, u"%-62s  %s" % (entry,
                                                format_duration_long(duration))
            print >> output
        print >> output, ("Total work done: %s" %
                          format_duration_long(total_work))
        print >> output
        if slack:
            for start, entry, duration in slack:
                entry = entry[:1].upper() + entry[1:]
                print >> output, u"%-62s  %s" % (entry,
                                                format_duration_long(duration))
            print >> output
        print >> output, ("Time spent slacking: %s" %
                          format_duration_long(total_slacking))

    def print_today(self, show_most_recent=True):
        items = list(self.all_entries())
        if not items:
            print "No work done today."
            return
        start, stop, duration, entry = items[0]
        entry = entry[:1].upper() + entry[1:]
        if show_most_recent:
            print "Most recent entry: %s at %s" % (entry, start.strftime('%H:%M'))
            print
        work, slack = self.grouped_entries()
        lengths = [len(entry[1]) for entry in work + slack]
        lengths.sort()
        if lengths:
            max_length = lengths[-1]
        else:
            max_length = 20
        total_work, total_slacking = self.totals()
        if work:
            output = []
            for start, entry, duration in work:
                entry = entry[:1].upper() + entry[1:]
                format = u"%-" + unicode(max_length) + u"s  %s"
                output.append(format % (entry,
                                        format_duration_long(duration)))
            output.sort()
            print '\n'.join(output)
            print
        print ("Total work done: %s" %
                          format_duration_long(total_work))
        print
        if slack:
            for start, entry, duration in slack:
                entry = entry[:1].upper() + entry[1:]
                print u"%-62s  %s" % (entry,
                                                format_duration_long(duration))
            print
        print ("Not-work-time:: %s" %
                          format_duration_long(total_slacking))

    def weekly_report(self, output, email, who, estimated_column=False):
        """Format a weekly report.

        Writes a weekly report template in RFC-822 format to output.
        """
        week = self.min_timestamp.strftime('%V')
        print >> output, "To: %(email)s" % {'email': email}
        print >> output, "Subject: Weekly report for %s (week %s)" % (who,
                                                                      week)
        print >> output
        items = list(self.all_entries())
        if not items:
            print >> output, "No work done this week."
            return
        print >> output, " " * 46,
        if estimated_column:
            print >> output, "estimated       actual"
        else:
            print >> output, "                time"
        work, slack = self.grouped_entries()
        total_work, total_slacking = self.totals()
        if work:
            work = [(entry, duration) for start, entry, duration in work]
            work.sort()
            for entry, duration in work:
                if not duration:
                    continue  # skip empty "arrival" entries
                entry = entry[:1].upper() + entry[1:]
                if estimated_column:
                    print >> output, (u"%-46s  %-14s  %s" %
                                (entry, '-', format_duration_long(duration)))
                else:
                    print >> output, (u"%-62s  %s" %
                                (entry, format_duration_long(duration)))
            print >> output
        print >> output, ("Total work done this week: %s" %
                          format_duration_long(total_work))


class TimeLog(object):
    """Time log.

    A time log contains a time window for today, and can add new entries at
    the end.
    """

    def __init__(self, filename, virtual_midnight):
        self.filename = filename
        self.virtual_midnight = virtual_midnight
        self.reread()

    def reread(self):
        """Reload today's log."""
        self.day = virtual_day(datetime.datetime.now(), self.virtual_midnight)
        min = datetime.datetime.combine(self.day, self.virtual_midnight)
        max = min + datetime.timedelta(1)
        self.history = []
        self.window = TimeWindow(self.filename, min, max,
                                 self.virtual_midnight,
                                 callback=self.history.append)
        self.need_space = not self.window.items

    def window_for(self, min, max):
        """Return a TimeWindow for a specified time interval."""
        return TimeWindow(self.filename, min, max, self.virtual_midnight)

    def whole_history(self):
        """Return a TimeWindow for the whole history."""
        # XXX I don't like this solution.  Better make the min/max filtering
        # arguments optional in TimeWindow.reread
        return self.window_for(self.window.earliest_timestamp,
                               datetime.datetime.now())

    def raw_append(self, line):
        """Append a line to the time log file."""
        f = open(self.filename, "a")
        if self.need_space:
            self.need_space = False
            print >> f
        print >> f, line
        f.close()

    def append(self, entry):
        """Append a new entry to the time log."""
        now = datetime.datetime.now().replace(second=0, microsecond=0)
        last = self.window.last_time()
        if last and different_days(now, last, self.virtual_midnight):
            # next day: reset self.window
            self.reread()
        self.window.items.append((now, entry))
        line = '%s: %s' % (now.strftime("%Y-%m-%d %H:%M"), entry)
        self.raw_append(line)


def print_day(day, timelog):
    min = datetime.datetime.combine(day, VIRTUAL_MIDNIGHT)
    max = min + datetime.timedelta(1)
    info = timelog.window_for(min, max)
    info.print_today()


def main():
    """Run the program."""
    if 'week' in sys.argv:
        printWeek = True
    else:
        printWeek = False
    configdir = os.path.expanduser('~/.gtimelog')
    try:
        os.makedirs(configdir)  # create it if it doesn't exist
    except OSError:
        pass
    timelog = TimeLog(os.path.join(configdir, 'timelog.txt'),
                      VIRTUAL_MIDNIGHT)
    today = datetime.datetime.now()
    if printWeek is False:
        day = virtual_day(today, VIRTUAL_MIDNIGHT)
        print_day(day, timelog)
    else:
        now = datetime.datetime.now()
        thirty_days = range(30)
        thirty_days.reverse()
        for nDays in thirty_days:
            day = now - datetime.timedelta(nDays)
            print
            print "*********************"
            print "** %s **" % day.strftime('%a %Y-%m-%d')
            print_day(day, timelog)

        # last sunday-now
        # .totals()
        cal = calendar.Calendar()
        weeks = cal.monthdatescalendar(today.year, today.month)
        if today.day < 15:
            # Also add the previous month.
            in_last_month = today - datetime.timedelta(days=20)
            last_months_weeks = cal.monthdatescalendar(in_last_month.year,
                                                       in_last_month.month)
            weeks = last_months_weeks + weeks

        print "\n\n\n\nWeekly overview"
        print "===============\n"
        for week in weeks:
            mon = week[0]
            sun = week[6]
            first = datetime.datetime(mon.year, mon.month, mon.day)
            if today < first:
                # Future week, don't bother.
                continue
            last = datetime.datetime(sun.year, sun.month, sun.day)
            info = timelog.window_for(first, last)
            worked, slacked = info.totals()
            total = (worked.seconds / 60.0 / 60) + (worked.days * 24)
            print "\nWeek %s van %s-%02s-%02s: %s uur" % (
                mon.strftime('%V'), mon.year, mon.month, mon.day, total)
            print "--------------------------------\n"

            info.print_today(show_most_recent=False)
            print

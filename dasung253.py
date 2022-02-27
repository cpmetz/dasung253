"""
Copyright 2022, Philip Metzler

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
associated documentation files (the "Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

import argparse
import serial
import time

def send_and_drain(s, message):
    s.write(message)
    str = s.read(24)
    print(str)

def main():
    parser = argparse.ArgumentParser(description='Paperlike 253 COM Port control')

    parser.add_argument('--port', dest='port', action='store', required=True)
    parser.add_argument('--threshold', dest='threshold', action='store', type=int, choices=range(0, 8), metavar="[0-7]")
    parser.add_argument('--clear', dest='clear', action='store_true', default=False)
    parser.add_argument('--mode', dest='mode', action='store', choices=['text', 'graphic', 'video'])
    parser.add_argument('--speed', dest='speed', action='store', type=int, choices=range(0, 5), metavar="[0-4]")
    args = parser.parse_args()

    baud_rate = 115200

    threshold = [
        b'5FF50101000000000000A0FA',
        b'5FF50102000000000000A0FA',
        b'5FF50103000000000000A0FA',
        b'5FF50104000000000000A0FA',
        b'5FF50105000000000000A0FA',
        b'5FF50106000000000000A0FA',
        b'5FF50107000000000000A0FA',
        b'5FF50109000000000000A0FA'
    ]

    modes = {
        'text': b'5FF50202000000000000A0FA',
        'graphic': b'5FF50203000000000000A0FA',
        'video': b'5FF50203000000000000A0FA'
    }

    clear_ghosting = b'5FF50300000000000000A0FA'

    speed = [
        b'5FF50401000000000000A0FA',
        b'5FF50402000000000000A0FA',
        b'5FF50403000000000000A0FA',
        b'5FF50404000000000000A0FA',
        b'5FF50405000000000000A0FA'
    ]

    s = serial.Serial(args.port, baud_rate, timeout = 1)

    should_clear = args.clear

    if args.threshold is not None:
        send_and_drain(s, threshold[args.threshold])

    if args.mode is not None:
        send_and_drain(s, modes[args.mode])
        str = s.read(24)  # The monitor will respond some more stuff. Ignore it.
        # Need to wait before sending the clear to get rid of the info box.
        time.sleep(3)
        should_clear = True

    if args.speed is not None:
        send_and_drain(s, speed[args.speed])
        # Need to wait before sending the clear to get rid of the info box.
        time.sleep(3)
        should_clear = True

    if should_clear:
        send_and_drain(s, clear_ghosting)

    s.close()

if __name__ == "__main__":
    main()

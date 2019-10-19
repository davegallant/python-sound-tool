import argparse
import os
from pydub import AudioSegment


def change_speed(segment, speed=1.0):
    new_segment = segment._spawn(
        segment.raw_data, overrides={"frame_rate": int(segment.frame_rate * speed)}
    )
    new_segment.set_frame_rate(segment.frame_rate)
    return new_segment


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("-s", "--speed", default=0.8, type=float)
    parser.add_argument("-f", "--file", required=True, type=str)

    args = parser.parse_args()

    filename, file_ext = os.path.splitext(args.file)
    segment = AudioSegment.from_file(args.file)

    new_segment = change_speed(segment, args.speed)
    export_path = "%s-%sx.%s" % (filename, args.speed, file_ext[1:])

    print("Modifying sound to be %sx speed." % args.speed)
    print("Exporting modified sound file to: %s" % export_path)

    new_segment.export(export_path, format=file_ext[1:])


main()

#!/usr/bin/env python
import click


@click.command()
@click.option('--floors', default=2, help='No. of floors hotel has')
@click.option('--main_cor', default=1, help='No. of main corridors per floor')
@click.option('--sub_cor', default=2, help='No. of sub corridors per floor')
@click.option('--sensor_state', default=False, type=bool, help='Boolean to indicate if any sensors are installed')
@click.argument('sensor_input', type=click.File('rb'))
def main(floors, main_cor, sub_cor, sensor_state, sensor_input):
    print 'Hotel statistics:'
    print 'Total floors = ' + str(floors)
    print 'Main corridors per floor = ' + str(main_cor)
    print 'Sub corridors per floor = ' + str(sub_cor)
    print 'Sensors installed: = ' + str(sensor_state)
    print 'FILE CONTENTS = '
    while True:
        line = sensor_input.readline()
        if not line:
            break
        print line


if __name__ == '__main__':
    main()

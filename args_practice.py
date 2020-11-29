# coding=utf-8

import sys
import argparse
import cliargs as cli


def payments(s, m, x):
    month_rate = (float(x) / 100) / 12
    payment = s * (month_rate + (month_rate/((1 + month_rate)**m - 1)))
    total_percent = 0
    sum = s
    for month in range(m):
        debt_payment = payment - (sum * month_rate)
        print(str(month + 1) + " " + str(round(sum, 2)) + " " + str(round(sum * month_rate, 2))
                    + " " + str(round(debt_payment, 2)) + " " + str(round(payment, 2)) + "\n")
        total_percent += sum * month_rate
        sum -= debt_payment
    print("Проценты: " + str(round(total_percent, 2)) + "\n" + "Полный платеж: "
               + str(round(total_percent + s, 2)))


def create_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument('mode', choices=['auto', 'not_auto'], default='auto', help='Choose 1 of 2 modes')
    parser.add_argument('s', type=int, nargs='?', default=1000, help='Sum parameter')
    parser.add_argument('m', type=int, nargs='?', default=12,
                        help='Number of months required')
    parser.add_argument('p', nargs='?', default=20, help='Percent parameter')

    return parser


def auto(**kwargs):
    print(payments(namespace.s, namespace.m, namespace.p))
    print("Сценарий: {}\n".format(kwargs['mode']))


def not_auto(**kwargs):
    namespace = parser.parse_args(sys.argv[1:])
    try:
        if sys.argv[2] and sys.argv[3] and sys.argv[4] is not None:
            print(payments(namespace.s, namespace.m, namespace.p))
            print("Сценарий: {}\n".format(kwargs['mode']))
    except IndexError:
        print("Ошибка")



if __name__ == "__main__":
    modes = {'auto': auto, 'not_auto': not_auto}

    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])

    args_dict = cli.argsAsDict(parser.parse_args()._get_kwargs())

    modes[args_dict['mode']](**args_dict)


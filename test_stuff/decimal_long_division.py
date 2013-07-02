import math
import stop_watch


def find_power(n, d):
    d_raised_to_power = d
    power = 0
    while True:
        d_raised_to_power_next = 10 * d_raised_to_power
        if d_raised_to_power_next < n:
            d_raised_to_power = d_raised_to_power_next
            power += 1
        else:
            break
    return d_raised_to_power, power


def find_multiplier(n, val):
    temp_sum = val
    multiplier = 1

    while True:
        temp_sum_next = temp_sum + val
        if temp_sum_next > n:
            break
        else:
            temp_sum = temp_sum_next
            multiplier += 1
    return temp_sum, multiplier


def long_division(n, d):
    n_sign = int(math.copysign(1, n))
    d_sign = int(math.copysign(1, d))
    remainder = abs(n)
    d = abs(d)
    quotient = 0
    while True:
        if d > remainder:
            break
        else:
            d_raised_to_power, power = find_power(remainder, d)
            amount_to_remove, multiplier = find_multiplier(remainder, d_raised_to_power)
            remainder -= amount_to_remove
            quotient += multiplier * 10 ** power
            # print d_raised_to_power, power, amount_to_remove, multiplier, quotient, remainder
    if n_sign != d_sign and remainder != 0:
        quotient += 1
        remainder -= d
        remainder *= -1
    # print quotient, remainder
    return n_sign * d_sign * quotient, d_sign * remainder


def run_test_loop(dividend_max, divisor_max):
    def do_test(n, d):
        q1, r1 = long_division(n, d)
        q2, r2 = divmod(n, d)
        assert (q1 == q2) and (r1 == r2)

        # div_string = '%4d/%4d' % (n, d)
        # result_string = '%5d %5d' % (q1, r1)
        # print '%10s: %s' % (div_string, result_string)

    time_stamper = stop_watch.StopWatch()
    time_stamper.record_time_stamp()

    total_tests = 0
    print dividend_max, divisor_max
    for n in xrange(1, dividend_max + 1):
        if n % 100 == 0:
            # time_stamper.record_time_stamp()
            print 'n: %d' % n
            # print n, time_stamper.get_last_gap()
        for d in xrange(1, min(n, divisor_max) + 1):
            total_tests += 1
            if total_tests % 100000 == 0:
                time_stamper.record_time_stamp()
                print '\tts: %5d; %s' % (time_stamper.get_num_timestamps(), time_stamper.get_last_gap())
            do_test(n, d)
            do_test(-n, -d)
            do_test(n, -d)
            do_test(-n, d)
            # print

            # q, r = long_division(n, d)
            # q2, r2 = divmod(n, d)
            # result_is_correct = (q == q2) and (r == r2)
            # fraction_string = '%d/%d' % (n, d)
            # if not result_is_correct:
            #     print '%15s %5d %5d %5s' % (fraction_string, q, r, result_is_correct)
    print total_tests


def main():
    run_test_loop(1500, 50)


main()

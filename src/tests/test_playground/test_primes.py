import unittest

from src.main.primes.primes import Primes, is_prime

PRIMES = [
    int(x)
    for x in """2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
101
103
107
109
113
127
131
137
139
149
151
157
163
167
173
179
181
191
193
197
199
211
223
227
229
233
239
241
251
257
263
269
271
277
281
283
293
307
311
313
317
331
337
347
349
353
359
367
373
379
383
389
397
401
409
419
421
431
433
439
443
449
457
461
463
467
479
487
491
499
503
509
521
523
541""".splitlines()
]


NON_PRIMES = [x for x in range(0, 541) if not x in PRIMES]


class TestPrimes(unittest.TestCase):
    def test_primes(self):
        for p in PRIMES:
            self.assertTrue(is_prime(p))

    def test_non_primes(self):
        for np in NON_PRIMES:
            self.assertFalse(is_prime(np), f"Unexpected result for {np}")

    def test_primes0(self):
        for p in PRIMES:
            self.assertEqual("true", Primes(p))

    def test_primes1(self):
        for p in NON_PRIMES:
            self.assertEqual("false", Primes(p))

    # def test_non_primes1(self):
    #     for np in NON_PRIMES:
    #         self.assertFalse(is_prime(np), f"Unexpected result for {np}")

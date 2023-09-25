# NHS Number Validator

The NHS NUMBER, the primary identifier of a PERSON, is a unique identifier for a PATIENT within the NHS in England and Wales.

The NHS NUMBER is 10 numeric digits in length. The tenth digit is a check digit used to confirm its validity.

The check digit is validated using the Modulus 11 algorithm and the use of this algorithm is mandatory.

## Steps

1. Multiply each of the first nine digits by a weighting factor as follows:

	1 -> 10
	2 -> 9
	3 -> 8
	4 -> 7
	5 -> 6
	6 -> 5
	7 -> 4
	8 -> 3
	9 -> 2

2. Add the results of each multiplication together.

3. Divide the total by 11 and establish the remainder.

4. Subtract the remainder from 11 to give the check digit.

5. Check the remainder matches the check digit. If it does not, the NHS NUMBER is invalid.

## Get Started

You can use the script to generate a valid NHS number or to validate a NHS number.

To generate:
```bash
python nhs_number.py
```

To validate:
```bash
python nhs_number.py <number_to_check>
```

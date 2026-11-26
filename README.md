CV Clean
========

This project was developed for [CV Heap LLC](https://cvheap.net/) in order to
ensure that any data seen by AI does not have any information that could
introduce any sort of hidden bias, without losing any important context.

This allows us to focus on high quality matches without sacrificing privacy.

Sanitization
------------

1. Remove anything that identifies the subject (PII/PHI)
2. Remove anything that reveals a protected class, while keeping the work
3. Tokenize organizations, people and products, and remove places
4. Collapse dates into durations and decay hints
5. Remove version numbers, then reduce every other number to two significant
   digits

See [Sanitization Rules](./RULES.md) for complete details.

Usage
-----

Command line:
```sh
# Using stdin
echo "Imaginary File Contents" | python3 -m cvclean

# Providing an input file
python3 -m cvclean -i imaginary_input.txt
```

Python module:
```python
sanitized_content = cvclean.apply_filters(original_content)
```

[[license](./LICENSE.txt)]

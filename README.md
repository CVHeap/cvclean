CV Clean
========

This project was developed for [CV Heap LLC](https://cvheap.net/) in order to
ensure that any data seen by AI does not have any information that could
introduce any sort of hidden bias, without losing any important context.

This allows us to focus on high quality matches without sacrificing privacy.

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

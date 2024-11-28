# What are tags?

Tags can represent several different concepts:

* Tags represent tainted data (e.g., positive tag means data potentially propagates the value forwards, leaking it). Assert that the tag is "always negative".
* Tags represent trusted/untrusted data (e.g., positive tag means the data has been affected by untrusted data). Assert that the tag is "always negative".

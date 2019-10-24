# pseudon
Simple tool I made to pseudonymize data in a specified column in a CSV file. Works fine with numeric data, could need some more thinking and improvement how to handle text data.

Pseudonymization of data can be used for example when creating test data from real world data.
The pseudonymization process encrypts data using a random (almost) AES128 key and format preserving encryption (FPE),
which means that the data keeps the same format. The FPE is done using [libffx](https://github.com/emulbreh/pyffx). 

(Pseudonymization does **not** mean that the data is anonymized (where identifiable data is destructed). Even if the key
not is stored, it can be possible to reconstruct the data using additional data. If psudonymized real-world data is used
for, for exampl, testing purposes, it should **never** be distributed or shared anywhere. Be careful with data)

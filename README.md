# Logfile Converter
Convert log file into json or plain text file.

## How to
```
$ python run.py <path/to/sourcefile.log> -t <target format> -o <output file>
```

## Use Cases

| # | Target | Output | Result | Destination |
| --- |---|---|---|---|
| 1. | None | None | txt| src_dir |
| 2. | text | None | txt| src_dir |
| 3. | json | None | json| src_dir |
| 4. | text | *.json | ValueError | x |
| 5. | json | *.txt | ValueError | x |
| 6. | text | *.txt | txt | dest_dir |
| 7. | json | *.json | json | dest_dir |
| 8. | None | *.json | ValueError | x |
| 9. | None | *.txt | txt | dest_dir |


src_dir: Source directory.  
dest_dir: Output destination directory.
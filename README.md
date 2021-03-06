# Logfile Converter
Convert log file into json or plain text file.

## How to

### Basic usage
```
$ ./logconvert <path/to/sourcefile.log>
```
### Full usage
```
$ ./logconvert <path/to/sourcefile.log> -t <target format> -o <path/to/output/file>
```

## Create Symbolic Link (optional)

```
$ sudo cp logconvert /opt/
$ sudo ln -s /opt/logconvert /usr/bin/logconvert
```

### Basic Usage with the Symlink
```
$ logconvert <path/to/sourcefile.log>
```

<br >

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

### Note
src_dir: Source directory.  
dest_dir: Output destination directory.

## Development Note

This project demonstrates how to create CLI interface using Argparse in Python to convert logfiles to Json and Text. In terms of conversion of its content, it is not included in this scope because it requires an example of the contents of the logfile to be converted.

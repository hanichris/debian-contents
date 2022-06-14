# ✨Package Statistics ✨
Package statistics is a command-line tool that takes an architecture (e.g arm64, amd64, mips etc.) and downloads the compressed Contents file from a Debian mirror. It outputs the top 10 packages that have the most associated files with them.

<br>

# The What, Why and How
<p>The approach employed to develop the command-line tool was the Test Driven Development (TDD) process. The unit tests captured in the <b>test.py</b> file were first written out before the actual development of the command-line tool. This laid out a roadmap for the development process. The tests were then used as a metric to measure the success of the tool in performing the necessary tasks.</p>
<p>The TDD process allowed for the development of the tool to be done in an object-oriented way which ensured modularity of code and ease of code extensibility in future.</p>
<p>How the tool works is by first instantiating a <i>PackageStats class</i> which then downloads and stores a record of the different system architectures available from the Debian mirror site as well as the installer and gzip file names associated with each architecture. When an architecture is provided to the class instance, it first checks the validity of the parameter it has received before downloading the <b>Contents file</b> associated with that particular architecture.
</p>
<p>The downloaded file is parsed and the files associated with each package are summed up. This output is stored in memory in the form of an associative array before being sorted by the file count of each package. </p>
<p>The top 10 packages by file count are then printed to the terminal in descending order.
</p>

## Environment
<hr>
🐍 Python 3.9.5

<br>

## ⬇️ Install dependencies
```zsh
python3 -m venv debian
source venv/bin/activate
pip install -r requirements.txt
```
<br>

## Using Package Statistics
As an example of how to use the command-line tool, execute the following on a terminal using the "amd64" system architecture as a test argument
```zsh
./package_statistics.py amd64
```
to get the following output
```zsh
#                         Package      File Count

 1.                         piglit      51784 files
 2.                  esys-particle      18015 files
 3.               libboost1.74-dev      14332 files
 4.                     acl2-books      12668 files
 5.                golang-1.15-src       9015 files
 6.            liboce-modeling-dev       7457 files
 7.                     zoneminder       7002 files
 8.                   paraview-dev       6178 files
 9.  linux-headers-5.10.0-13-amd64       6149 files
10.  linux-headers-5.10.0-10-amd64       6148 files
```

## Testing
If you are using the Microsoft Visual Studio Code IDE, support for unittest execution is built in. Open the command pallete and type 'Python test.' Choose <i>Debug All Unit Tests</i> and VSCode will raise a prompt to configure the test framework. Click on the cog to select the test runner (unittest) and the appropriate directory.

### Miscellaneous
The overall time spent in the development of this command-line tool was 2 days.
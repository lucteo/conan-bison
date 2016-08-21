from conans import ConanFile, ConfigureEnvironment
from conans.tools import download, unzip, untargz
import os

class BisonConan(ConanFile):
    name = "bison"
    version = "3.0.4"
    url = "https://github.com/lucteo/conan-bison.git"
    license = "GNU General Public License: https://www.gnu.org/licenses/gpl.html"
    settings = "os", "compiler", "build_type", "arch"
    exports = "*"

    archiveName = "bison-3.0.4.tar.gz"
    folderName = "bison-3.0.4"

    def source(self):
        download("http://ftp.gnu.org/gnu/bison/" + self.archiveName, self.archiveName)
        untargz(self.archiveName)
        os.unlink(self.archiveName)
        if self.settings.os != "Windows":
            self.run("chmod +x ./%s/configure" % self.folderName)

    def build(self):
        if self.settings.os == "Linux" or self.settings.os == "Macos":
            env = ConfigureEnvironment(self.deps_cpp_info, self.settings)
            env_line = env.command_line
                        
            self.run("cd %s && %s ./configure --prefix=%s/out" % (self.folderName, env_line, self.conanfile_directory))
            self.run("cd %s && %s make" % (self.folderName, env_line))            
            self.run("cd %s && %s make install " % (self.folderName, env_line))            

    def package(self):
        self.copy("*", dst="", src="out")

    def package_info(self):
        # Don't list the libraries generated; bison is mainly used as a tool
        # self.cpp_info.libs = ['y']  # The libs to link against
        # self.cpp_info.libdirs = ['lib']  # Directories where libraries can be found
        self.cpp_info.resdirs = ['share/bison']  # Directories where resources, data, etc can be found
        self.cpp_info.bindirs = ['bin']  # Directories where executables and shared libs can be found

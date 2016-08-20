from conans import ConanFile, CMake
import os

############### CONFIGURE THESE VALUES ##################
default_user = "lucteo"
default_channel = "testing"
#########################################################

channel = os.getenv("CONAN_CHANNEL", default_channel)
username = os.getenv("CONAN_USERNAME", default_user)

class TestBisonConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "bison/3.0.4@%s/%s" % (username, channel)
    generators = "cmake"

    def build(self):
        cmake = CMake(self.settings)
        self.output.info("Running CMake")
        self.run('cmake "%s" %s' % (self.conanfile_directory, cmake.command_line))
        self.output.info("Building the bison test project")
        self.run("cmake --build . %s" % cmake.build_config)

    def test(self):
        self.output.info("Running smoke test (expecting 7)")
        testArg = "1 + 2* 3"
        self.run('echo "%s" | ./bin/test-bison' % testArg)

[![Build Status](https://travis-ci.org/lucteo/conan-bison.svg)](https://travis-ci.org/lucteo/conan-bison)
[![Build Status](https://ci.appveyor.com/api/projects/status/github/lucteo/conan-bison)](https://ci.appveyor.com/project/lucteo/conan-bison)


# conan-bison
[Conan.io](https://conan.io) package for BISON.

Thanks for [lasote](https://github.com/lasote) for providing example on building this package. 

The packages generated with this **conanfile** can be found in [conan.io](https://conan.io/source/bison/3.0.4/lucteo/stable).

## Build packages

    $ pip install conan_package_tools
    $ python build.py
    
## Upload packages to server

    $ conan upload bison/3.0.4@lucteo/stable --all
    
## Reuse the packages

### Basic setup

    $ conan install bison/3.0.4@lucteo/stable
    
### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*
    
    [requires]
    bison/3.0.4@lucteo/stable

    [generators]
    txt
    cmake

Complete the installation of requirements for your project running:</small></span>

    conan install . 

Project setup installs the library (and all his dependencies) and generates the files *conanbuildinfo.txt*.

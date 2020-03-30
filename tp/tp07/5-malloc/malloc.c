
/**
 * SO, 2017
 * Lab #6
 *
 * Task #1, lin
 *
 * Use of pmap for showing different behavior of mmap calls
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <sys/wait.h>

#include "utils.h"

#define NUM_PAGES 4

static void wait_for_input(const char *msg)
{
	char buf[32];

	printf(" * %s\n", msg);
	printf(" -- Press ENTER to continue ...\n"); fflush(stdout);
	fgets(buf, 32, stdin);
}

int main(void)
{
	*i = malloc (4*1024*1024 * sizeof (int));

	wait_for_input("allocated a 4 MB memory space");

	i[0] = 1;

	return 0;
}


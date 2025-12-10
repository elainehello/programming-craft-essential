#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include "common.h"

int counter = 0;
int loops;
pthread_mutex_t counter_mutex = PTHREAD_MUTEX_INITIALIZER;

/**
 * @brief Worker thread that increments the global counter `loops` times.
 *
 * @param arg Pointer passed to the thread (unused, may be NULL).
 * @return Returns NULL on completion.
 */
void* worker(void *arg)
{
    (void)arg;
    int i;
    for (i = 0; i < loops; ++i) {
        pthread_mutex_lock(&counter_mutex);
        counter++;
        pthread_mutex_unlock(&counter_mutex);
    }
    return NULL;
}

/**
 * @brief Program entry point that starts two worker threads.
 *
 * @param argc Number of command-line arguments.
 * @param argv Argument vector; `argv[1]` should contain the loop count.
 * @return Returns 0 on success, non-zero on error.
 */
int main(int argc, char **argv)
{
    pthread_t p1;
    pthread_t p2;

    if (argc != 2) {
        fprintf(stderr, "Usage: %s <value>\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    loops = atoi(argv[1]);

    printf("Starting threads...\n");
    printf("Loops: %d\n", loops);
    printf("Initial value: %d\n", counter);

    if (pthread_create(&p1, NULL, worker, NULL) != 0) {
        perror("pthread_create p1");
        exit(EXIT_FAILURE);
    }
    if (pthread_create(&p2, NULL, worker, NULL) != 0) {
        perror("pthread_create p2");
        exit(EXIT_FAILURE);
    }
    if (pthread_join(p1, NULL) != 0) {
        perror("pthread_join p1");
        exit(EXIT_FAILURE);
    }
    if (pthread_join(p2, NULL) != 0) {
        perror("pthread_join p2");
        exit(EXIT_FAILURE);
    }

    printf("Final value: %d\n", counter);
    return 0;
}

/* /# gcc threads.c -o threads -Wall -lpthread */

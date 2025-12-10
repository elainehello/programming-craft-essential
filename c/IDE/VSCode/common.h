#ifndef COMMON_H
#define COMMON_H

#include <pthread.h>

#ifdef __cplusplus
extern "C" {
#endif

/**
 * @brief Thread worker function that increments the global counter.
 *
 * @param arg Pointer passed to the thread (unused, may be NULL).
 * @return Always returns NULL.
 */
void *worker(void *arg);

#ifdef __cplusplus
}
#endif

#endif /* COMMON_H */

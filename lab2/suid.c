#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

void report (uid_t real) {
    printf (
        "Real UID: %d Effective UID: %d\n",
        real,
        geteuid()
    );
}

int main (void) {
    uid_t real = getuid();
    report(real);
    return 0;
}

#include "obfuscate.h"

// Returns the obfuscated key.
extern "C" {
const char *get_key() {
  const char *obfuscatedKey = AY_OBFUSCATE("vocab-tester");
  return obfuscatedKey;
}
}

#include "../_vendor/Obfuscate/obfuscate.h"

extern "C" {
const char *get_key() {
  /**
   * This function returns the obfuscated ksey.
   * Note that when the code is compiled, the key is obfuscated.
   * It can probably still be extracted by a determined attacker, but
   * it will do for this simple project.
   * (And of course, the key is available to see right here.)
   */

  const char *obfuscatedKey = AY_OBFUSCATE("vocab-tester-key");
  return obfuscatedKey;
}
}

int main() { return 0; }

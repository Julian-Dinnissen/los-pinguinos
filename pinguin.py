pinguin2024_int = 40_000_000
geboorte_int = 2_000_000

mensen2023_int = 7_942_645_086
mensen2024_int = 8_019_876_189

mensgeboorte2023_int = 131_487_375
menssterfte2023_int = 61_062_674


def groei(nieuw, oud):
  return (nieuw - oud) / oud


groeifactor = groei(mensen2024_int, mensen2023_int)
pinguin2023_int = pinguin2024_int - pinguin2024_int * groeifactor

print(pinguin2023_int)

print("Welkom \n amongus")
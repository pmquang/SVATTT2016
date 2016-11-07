
int __cdecl main(int a1, char **a2)
{
  int result; // eax@7
  size_t v3; // [sp+14h] [bp-Ch]@3
  const char *v4; // [sp+18h] [bp-8h]@3

  if ( a1 <= 1 )
    exit(-1);
  v3 = strlen(a2[1]);
  v4 = a2[1];
  if ( v4[v3 - 1] == 10 )
    v4[v3 - 1] = 0;
  if ( strlen(v4) != 8 )
    exit(-1);
  result = strtoul(v4, 0, 17);
  if ( result == 53 )
    result = printf("SVATTT{%s}\n", v4);
  return result;
}

len(key) = 8
convert base-10 -> base-17 
	53 	-> 32

./ze 00000032
flag: SVATTT{00000032}

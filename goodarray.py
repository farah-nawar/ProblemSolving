def removeDuplicates(s, ch):

  if (len(s) <= 1):
    return s
  i = 0
  while (i < len(s)):
    if (i + 1 < len(s) and s[i] == s[i + 1]):
      j = i
      while (j + 1 < len(s) and s[j] == s[j + 1]):
        j += 1

      lastChar = s[i - 1] if (i > 0) else ch

      remStr = removeDuplicates(s[j + 1: len(s)], lastChar)

      s = s[0: i]
      k, l = len(s), 0
      while (len(remStr) > 0 and len(s) > 0
             and remStr[0] == s[len(s) - 1]):
        while (len(remStr) > 0
               and remStr[0] != ch
               and remStr[0] == s[len(s) - 1]):
          remStr = remStr[1: len(remStr) + 1]

        s = s[0: len(s) - 1]
      s = s + remStr
      i = j
    else:
      i += 1
  return s

if __name__ == '__main__':
  n=int(input())
  lst=[int(x) for x in input().split()]
  print(*removeDuplicates(lst,' '))



unsigned sequence_sum(unsigned start, unsigned end, unsigned step)
{
  unsigned int sum = 0;
  for(; start <= end ;sum += start ,start +=step){}
  return sum;
}
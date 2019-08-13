unsigned long long firstkdigits(int num, int k) 
{ 
   unsigned long long product = 1; 
  
   for (int i = 0 ; i < num ; i++) 
      product *= num; 
  
   while ((int)(product / pow(10, k)) != 0) 
      product = product / 10; 
  
   return product; 
} 
  
int main() 
{ 
   int num = 15; 
   int k = 4; 
   cout << firstkdigits(num, k); 
   return 0; 
} 

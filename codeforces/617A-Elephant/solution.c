#include<stdio.h>
 
int main(){
	
	int coordinate, p = 0;
	
	scanf("%i",&coordinate);
	
	for(int i=0; i<coordinate; i++){
		if (i%5==0){
			p++;
		}
	}
	printf("%i",p);
	
	return 0;
} 

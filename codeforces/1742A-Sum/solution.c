#include<stdio.h>
 
int main(){
	
	int t, a, b, c;
	
	scanf("%i",&t);
	
	for(int i = 0; i < t; i++) {
		scanf("%i %i %i",&a, &b, &c);
		if ( a + b == c) {
			printf("Yes\n");
		}else if (a + c == b) {
			printf("Yes\n");
		}else if ( b + c == a) {
			printf("Yes\n");
		}else {
			printf("No\n");
		}
	}
	return 0;
}

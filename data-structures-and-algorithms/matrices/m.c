#include <stdio.h>
#include <stdlib.h>

struct Matrix {
  int* A;
  int n;
};

void set(struct Matrix* m, int i, int j, int x){
    if (i*j >= 0 && i*j <= m->n*m->n){
        if (i==j) m->A[i-1] = x;
    }
    else printf("Invalid Index\n");
}

int get(struct Matrix m, int i, int j){
    if (i*j >= 0 && i*j <= m.n*m.n){
        if (i==j) return m.A[i-1];
        else return 0;
    }
    else {
        printf("Invalid Index\n");
        return -1;
    };
}

void display(struct Matrix m) {

    for(int i=0;i<m.n;i++){
        for(int j=0;j<m.n;j++){
            if(i==j) printf("%d ",m.A[i]);
            else printf("0 ");
        }
        printf("\n");
    }

}

int main() {

    struct Matrix m;

    int n = 5;
    m.n = n;
    m.A = (int*)malloc(m.n*sizeof(int));

    set(&m,1,1,5);set(&m,2,2,9);set(&m,3,3,8);set(&m,4,4,4);set(&m,5,5,7);

    display(m);

    printf("\n");

    printf("%d\n",get(m,3,3));
    printf("%d\n",get(m,1,2));

    free(m.A);
    
    return 0;
}

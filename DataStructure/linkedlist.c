#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>

struct Node {
  int data;
  struct Node* next;
};

int main(){
  printf("Hello, I am world\n");
  struct Node* head = NULL;
  struct Node* second = NULL;
  struct Node* third = NULL;

  head = (struct Node*) malloc(sizeof(struct Node));
  //head->next = (struct Node*) malloc(sizeof(struct Node) * 1);
  second = (struct Node*) malloc(sizeof(struct Node) * 1);
  //second->next = (struct Node*) malloc(sizeof(struct Node) * 1);
  third = (struct Node*) malloc(sizeof(struct Node) * 1);
  //third->next = (struct Node*) malloc(sizeof(struct Node) * 1);
  
  head->data = 1;
  head->next = second;

  second->data = 2;
  second->next = third;
 
  third->data = 3;
  third->next = NULL;
  printf("\n[head - date -> %d]\n| - -  [second - data -> %d ]\n | - - third - data ->  %d]\n", head->data, second->data, third->data); 
  return 0;
}



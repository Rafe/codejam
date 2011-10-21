#include<stdio.h>
#include<stdlib.h>
#include<string.h>

typedef struct node{
  int data;
  struct node* next;
} Node;

int checkDuplicate(Node* n){
  Node* i = n; 
  Node* j;
  while(i->next != NULL){
    j = i;
    while(j->next != NULL){
      j = j->next;
      if(i->data == j->data){
        return 1;
      }
    }
    i = i->next;
  }
  return 0;
}

Node* createNode(char data){
  Node* n = (Node*) malloc(sizeof(Node));
  n->data = data;
  n->next = NULL;
  return n;
}

void destoryNode(Node* node){
  if(node->next){
    destoryNode(node->next);
  }
  free(node);
}

int main(){
  Node* a = createNode(1);
  a->next = createNode(2);
  a->next->next = createNode(2);
  printf("%d",checkDuplicate(a));
  destoryNode(a);

  return 0;
}

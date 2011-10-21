#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define TABLE_WIDTH 20

typedef struct node{
  int data;
  struct node* next;
} Node;

Node* createNode(int data);
Node* appendNode(Node* node,int data);
int findNode(Node* node,int data);

int simpleHash(int value){
  return (value * 37 ) % TABLE_WIDTH;
}

Node* createNode(int data){
  Node* n = (Node*) malloc(sizeof(Node));
  n->data = data;
  n->next = NULL;
  return n;
}

Node* appendNode(Node* node,int data){
  if(node == NULL) {
    node = createNode(data);
    printf("append node:(%d)\n",data);
    return node;
  }  
  while(node->next != NULL){
    node = node->next;
  }
  node->next = createNode(data);
  return node;
}

int findNode(Node* node,int data){
  if(node == NULL) {
    return 0;
  }
  while(node != NULL){
    if(node->data == data){
      return 1;
    }
    node = node->next;
  }
  return 0;
}

void destoryNode(Node* node){
  if(node->next){
    destoryNode(node->next);
  }
  free(node);
}

int checkDuplicate(Node* n){
  if(n == NULL) return 0;

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

int checkDuplicateWithHash(Node* n){
  if(n == NULL) return 0;

  Node** table = calloc(TABLE_WIDTH,sizeof(Node*));
  int hash,i;
  
  //pitfall:dont manipulate pointer with address 0
  while(n != NULL){
    hash = simpleHash(n->data);
    if(findNode(table[hash],n->data)){
      return 1;
    }
    table[hash] = appendNode(table[hash],n->data);;
    n = n->next;
  }
  return 0;
}


int main(){
  Node* a = createNode(1);
  a->next = createNode(2);
  a->next->next = createNode(2);
  printf("check without hash::%d\n",checkDuplicate(a));
  printf("check with hash::%d\n",checkDuplicateWithHash(a));
  destoryNode(a);

  return 0;
}

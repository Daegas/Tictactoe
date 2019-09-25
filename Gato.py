# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 01:30:25 2019

@author: degamasandoval
"""

#Cuales son variables de instancia y cuales variables solo temporales en un método
#Para que sirve el 3er método en su algoritmo
#Como funciona score vs. moves
#Cuando usar self y cuando no
#Borrar prints
#borrar inputs start board=


import math

# =============================================================================
# Class
# =============================================================================

class tictactoe():
    def __init__(self): #instance variable
        self.board = []
        for i in range(9):
            self.board.append('')
        self.depth=9
        
        
    
    def genmoves(self,board): # list with indices of possible moves
        moves=[]
        for i in range(len(board)):
            if board[i] not in (True, False):
                moves.append(i)
        return moves
                
    def play(self): ##############################################
        self.cross=self.inputs(True,True) #First time? depth = 9 and asks for cross(Cross Default = True)
        
        while self.status(self.board) == 3: #While the board is not completed
            #------------Machine
            print('Thinking... \n')
            score=[]
            moves=self.genmoves(self.board) #index of possible moves
            
            print('moves', moves)
            for index in moves:
                fakeboard= self.board[:]
                self.move(index,not self.cross,fakeboard)
                score.append((index, self.alphabeta(fakeboard, self.depth, -math.inf, math.inf, False)))
            
            mv=(0,-1)
            for i in score:
                if i[1]>mv[1]:
                    mv=i
            print('score: ', score,'\n','mv: ',mv)
            self.move(mv[0], not self.cross,self.board)
            self.printboard(self.board)
            
            if self.status(self.board) in (1,0,-1):
                print('\t \t \t Game Over, You lose')
                
         #-----------------Player
            self.inputs(False,self.cross)
            if self.status(self.board) in (1,0,-1):
                print('\t \t \t You win')
            
            
            
    def alphabeta(self, board, depth, alpha, beta, maxplayer):
        #print('alpha:',board,maxplayer,self.status(board))
        if self.status(board) in (1,0,-1):#End of the game
            return self.status(board)
        elif depth==0:
            return 0
            
        t = self.genmoves(board)
              
        if maxplayer: #Machine
            val = -math.inf
            for child in t:
                fakeboard= board[:]
                self.move(child,not self.cross,fakeboard)
                #print('alpha tryin in: ', fakeboard, child )
                val = max(val, self.alphabeta(fakeboard, depth-1, alpha, beta, False)) # Vamos un nivel mas adentro, le toca al oponente
                alpha = max(alpha, val)
                if alpha >= beta:
                    break
                
            return val
    
        else:
            val = math.inf
            for child in t:
                fakeboard= board[:]
                self.move(child,self.cross,fakeboard) 
                #print('alpha tryin in: ', fakeboard, child )
                val = min(val, self.alphabeta(fakeboard, depth-1, alpha, beta, True)) # Vamos un nivel mas adentro, le toca a nuestro jugador
                beta = min(beta, val)
                if alpha >= beta:
                    break
            return val    
        
    
    
# Useful Methods =====================================
    def inputs(self,start,cross):
        if start:
            while True:
                inp =int(input('¿Qué símbolo eliges? Cruz= 1 o Círculo=0 \n'))
                if inp==1: 
                    cross=True
                    break
                elif inp==0: 
                    cross=False
                    break
                else: print('Opción Inválida')
        while True:
            inp = input('Elige tu movimiento Ejemplo: 2,2 \n')
            coord=(int(inp[0]),int(inp[2]))
            if (coord[0] and coord[1])<=2:
                if (coord[0] and coord[1])>=0:
                    self.move(coord, cross ,self.board)
                    break
            else: print('Movimiento Inválido')
        
        
        self.printboard(self.board)
        return cross
        
    
    def move(self,coord,cross,board):
        if type(coord)==tuple:
            coord= 3* coord[0] + coord[1]
        if board[coord] not in (True,False):
            board[coord]=cross
    
    
    
    def checklines(self,board,cross):
        line=False
        for i in range(3):
            if board[i]==cross and board[i+3] == cross and board[i+6]== cross: #Columns
                line=True
                break
            if i==0: #Diagonal
               if board[i]==cross and board[i+4] == cross and board[i+8]== cross:
                line=True
                break
            if i==2:#Diagonal
               if board[i]==cross and board[i+2] == cross and board[i+4]== cross:
                line=True
                break
        for i in range(0,9,3): #Lines
            if board[i]==cross and board[i+1] == cross and board[i+2]== cross:
                line=True
                break     
        return line
    
    def status(self,board): 
            #print('status:',board)
            if self.checklines(board, self.cross): #Player wins
                return -1
            elif self.checklines(board,not self.cross): #Machine wins
                return 1
            else:
                for i in board:
                    if i not in (True,False):
                        return 3 #Not completed
                    else:
                        continue
                return 0 #Draw      
            
    def printboard(self,board):
        temp=[]
        for i in range(len(board)):
            if board[i]==True: temp.append('X')
            elif board[i]==False: temp.append('O')
            else: temp.append(' ')
        for i in range(0,9,3):
            print('\t' ,temp[i], '|', temp[i+1],'|', temp[i+2])
# =============================================================================
# Main
# =============================================================================
ttt=tictactoe()
ttt.play()     
        
        

    
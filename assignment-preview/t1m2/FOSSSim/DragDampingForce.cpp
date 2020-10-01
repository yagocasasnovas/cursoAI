#include "DragDampingForce.h"

void DragDampingForce::addGradEToTotal( const VectorXs& x, const VectorXs& v, const VectorXs& m, VectorXs& gradE )
{
  assert( x.size() == v.size() );
  assert( x.size() == m.size() );
  assert( x.size() == gradE.size() );
  assert( x.size()%2 == 0 );
  
  // Your code goes here!
  
  //m_b
  
  int num_part = x.size()/2;
  
  for(int i = 0;i<num_part;i++)
  
  {
  
  gradE[2*i] += m_b*v[2*i];
  gradE[2*i+1] += m_b*v[2*i+1];
  
  
  
  
  }
  
  
}

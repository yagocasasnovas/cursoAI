#include "LinearizedImplicitEuler.h"
#include <iostream>
using namespace std;

//bool LinearizedImplicitEuler::stepScene( TwoDScene& scene, scalar dt )
//{
//  VectorXs& x = scene.getX();
//  VectorXs& v = scene.getV();
//  const VectorXs& m = scene.getM();
//  assert(x.size() == v.size());
//  assert(x.size() == m.size());

  // Your code goes here!
  
//  return true;
//}


bool LinearizedImplicitEuler::stepScene( TwoDScene& scene, scalar dt )
{
  VectorXs& x = scene.getX();
  VectorXs& v = scene.getV();
  const VectorXs& m = scene.getM();
  assert(x.size() == v.size());
  assert(x.size() == m.size());

  // Create diagonal mass matrix
  int dof = m.size();
  MatrixXs M(dof, dof);
  for (int i=0; i<m.size(); i++) {
    for (int j=0; j<m.size(); j++) {
      M(i,j) = (i == j) ? m(i) : 0;  //si i == j entonces m(i) en caso contrario 0
    }
  }

  // LHS  ¿?¿?
  
  
  MatrixXs A = MatrixXs::Zero(dof, dof);  //A = matriz de ceros?
  
  
  MatrixXs dUdxdx = MatrixXs::Zero(dof, dof);  // otra matriz de zeros
  
  scene.accumulateddUdxdx(dUdxdx, v * dt, VectorXs::Zero(dof));  //no se que pasa aquí. Pilla los gradientes de fuerza acumulados.
  
  
  dUdxdx *= pow(dt, 2);   //potencia de dt al cuadrado.   dUdxdx = dUdxdx * dt * dt
  
  //cout << pow(dt,2) << endl;
  
  //cout << dUdxdx << endl;
  
  scene.accumulateddUdxdv(A);
  A *= dt;
  A += dUdxdx;
  A = M - A;

  VectorXs F(dof);
  scene.accumulateGradU(F, v * dt, VectorXs::Zero(dof));
  for (int i=0; i<scene.getNumParticles(); i++) {
    if (scene.isFixed(i)) {
      F.segment<3>(3 * i).setZero();
      A.row(3 * i).setZero();
      A.row(3 * i + 1).setZero();
      A.row(3 * i + 2).setZero();
      A.col(3 * i).setZero();
      A.col(3 * i + 1).setZero();
      A.col(3 * i + 2).setZero();
    }
  }

  VectorXs dq = A.fullPivLu().solve(dt * F);
  v -= dq;
  x += dt * v;

  return true;
}
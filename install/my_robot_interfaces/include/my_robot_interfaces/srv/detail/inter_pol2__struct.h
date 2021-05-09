// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from my_robot_interfaces:srv/InterPol2.idl
// generated code does not contain a copyright notice

#ifndef MY_ROBOT_INTERFACES__SRV__DETAIL__INTER_POL2__STRUCT_H_
#define MY_ROBOT_INTERFACES__SRV__DETAIL__INTER_POL2__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in srv/InterPol2 in the package my_robot_interfaces.
typedef struct my_robot_interfaces__srv__InterPol2_Request
{
  double posx;
  double posy;
  double posz;
  double r;
  double p;
  double y;
  double time;
} my_robot_interfaces__srv__InterPol2_Request;

// Struct for a sequence of my_robot_interfaces__srv__InterPol2_Request.
typedef struct my_robot_interfaces__srv__InterPol2_Request__Sequence
{
  my_robot_interfaces__srv__InterPol2_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} my_robot_interfaces__srv__InterPol2_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'description'
#include "rosidl_runtime_c/string.h"

// Struct defined in srv/InterPol2 in the package my_robot_interfaces.
typedef struct my_robot_interfaces__srv__InterPol2_Response
{
  bool success;
  rosidl_runtime_c__String description;
} my_robot_interfaces__srv__InterPol2_Response;

// Struct for a sequence of my_robot_interfaces__srv__InterPol2_Response.
typedef struct my_robot_interfaces__srv__InterPol2_Response__Sequence
{
  my_robot_interfaces__srv__InterPol2_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} my_robot_interfaces__srv__InterPol2_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MY_ROBOT_INTERFACES__SRV__DETAIL__INTER_POL2__STRUCT_H_

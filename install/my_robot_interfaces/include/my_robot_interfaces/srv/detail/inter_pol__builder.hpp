// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from my_robot_interfaces:srv/InterPol.idl
// generated code does not contain a copyright notice

#ifndef MY_ROBOT_INTERFACES__SRV__DETAIL__INTER_POL__BUILDER_HPP_
#define MY_ROBOT_INTERFACES__SRV__DETAIL__INTER_POL__BUILDER_HPP_

#include "my_robot_interfaces/srv/detail/inter_pol__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace my_robot_interfaces
{

namespace srv
{

namespace builder
{

class Init_InterPol_Request_velocity
{
public:
  explicit Init_InterPol_Request_velocity(::my_robot_interfaces::srv::InterPol_Request & msg)
  : msg_(msg)
  {}
  ::my_robot_interfaces::srv::InterPol_Request velocity(::my_robot_interfaces::srv::InterPol_Request::_velocity_type arg)
  {
    msg_.velocity = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_robot_interfaces::srv::InterPol_Request msg_;
};

class Init_InterPol_Request_time
{
public:
  explicit Init_InterPol_Request_time(::my_robot_interfaces::srv::InterPol_Request & msg)
  : msg_(msg)
  {}
  Init_InterPol_Request_velocity time(::my_robot_interfaces::srv::InterPol_Request::_time_type arg)
  {
    msg_.time = std::move(arg);
    return Init_InterPol_Request_velocity(msg_);
  }

private:
  ::my_robot_interfaces::srv::InterPol_Request msg_;
};

class Init_InterPol_Request_wrist
{
public:
  explicit Init_InterPol_Request_wrist(::my_robot_interfaces::srv::InterPol_Request & msg)
  : msg_(msg)
  {}
  Init_InterPol_Request_time wrist(::my_robot_interfaces::srv::InterPol_Request::_wrist_type arg)
  {
    msg_.wrist = std::move(arg);
    return Init_InterPol_Request_time(msg_);
  }

private:
  ::my_robot_interfaces::srv::InterPol_Request msg_;
};

class Init_InterPol_Request_elbow
{
public:
  explicit Init_InterPol_Request_elbow(::my_robot_interfaces::srv::InterPol_Request & msg)
  : msg_(msg)
  {}
  Init_InterPol_Request_wrist elbow(::my_robot_interfaces::srv::InterPol_Request::_elbow_type arg)
  {
    msg_.elbow = std::move(arg);
    return Init_InterPol_Request_wrist(msg_);
  }

private:
  ::my_robot_interfaces::srv::InterPol_Request msg_;
};

class Init_InterPol_Request_shoulder
{
public:
  Init_InterPol_Request_shoulder()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_InterPol_Request_elbow shoulder(::my_robot_interfaces::srv::InterPol_Request::_shoulder_type arg)
  {
    msg_.shoulder = std::move(arg);
    return Init_InterPol_Request_elbow(msg_);
  }

private:
  ::my_robot_interfaces::srv::InterPol_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_robot_interfaces::srv::InterPol_Request>()
{
  return my_robot_interfaces::srv::builder::Init_InterPol_Request_shoulder();
}

}  // namespace my_robot_interfaces


namespace my_robot_interfaces
{

namespace srv
{

namespace builder
{

class Init_InterPol_Response_description
{
public:
  explicit Init_InterPol_Response_description(::my_robot_interfaces::srv::InterPol_Response & msg)
  : msg_(msg)
  {}
  ::my_robot_interfaces::srv::InterPol_Response description(::my_robot_interfaces::srv::InterPol_Response::_description_type arg)
  {
    msg_.description = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_robot_interfaces::srv::InterPol_Response msg_;
};

class Init_InterPol_Response_success
{
public:
  Init_InterPol_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_InterPol_Response_description success(::my_robot_interfaces::srv::InterPol_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return Init_InterPol_Response_description(msg_);
  }

private:
  ::my_robot_interfaces::srv::InterPol_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_robot_interfaces::srv::InterPol_Response>()
{
  return my_robot_interfaces::srv::builder::Init_InterPol_Response_success();
}

}  // namespace my_robot_interfaces

#endif  // MY_ROBOT_INTERFACES__SRV__DETAIL__INTER_POL__BUILDER_HPP_

// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from my_robot_interfaces:srv/InterPol2.idl
// generated code does not contain a copyright notice

#ifndef MY_ROBOT_INTERFACES__SRV__DETAIL__INTER_POL2__BUILDER_HPP_
#define MY_ROBOT_INTERFACES__SRV__DETAIL__INTER_POL2__BUILDER_HPP_

#include "my_robot_interfaces/srv/detail/inter_pol2__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace my_robot_interfaces
{

namespace srv
{

namespace builder
{

class Init_InterPol2_Request_shape
{
public:
  explicit Init_InterPol2_Request_shape(::my_robot_interfaces::srv::InterPol2_Request & msg)
  : msg_(msg)
  {}
  ::my_robot_interfaces::srv::InterPol2_Request shape(::my_robot_interfaces::srv::InterPol2_Request::_shape_type arg)
  {
    msg_.shape = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_robot_interfaces::srv::InterPol2_Request msg_;
};

class Init_InterPol2_Request_time
{
public:
  explicit Init_InterPol2_Request_time(::my_robot_interfaces::srv::InterPol2_Request & msg)
  : msg_(msg)
  {}
  Init_InterPol2_Request_shape time(::my_robot_interfaces::srv::InterPol2_Request::_time_type arg)
  {
    msg_.time = std::move(arg);
    return Init_InterPol2_Request_shape(msg_);
  }

private:
  ::my_robot_interfaces::srv::InterPol2_Request msg_;
};

class Init_InterPol2_Request_y
{
public:
  explicit Init_InterPol2_Request_y(::my_robot_interfaces::srv::InterPol2_Request & msg)
  : msg_(msg)
  {}
  Init_InterPol2_Request_time y(::my_robot_interfaces::srv::InterPol2_Request::_y_type arg)
  {
    msg_.y = std::move(arg);
    return Init_InterPol2_Request_time(msg_);
  }

private:
  ::my_robot_interfaces::srv::InterPol2_Request msg_;
};

class Init_InterPol2_Request_p
{
public:
  explicit Init_InterPol2_Request_p(::my_robot_interfaces::srv::InterPol2_Request & msg)
  : msg_(msg)
  {}
  Init_InterPol2_Request_y p(::my_robot_interfaces::srv::InterPol2_Request::_p_type arg)
  {
    msg_.p = std::move(arg);
    return Init_InterPol2_Request_y(msg_);
  }

private:
  ::my_robot_interfaces::srv::InterPol2_Request msg_;
};

class Init_InterPol2_Request_r
{
public:
  explicit Init_InterPol2_Request_r(::my_robot_interfaces::srv::InterPol2_Request & msg)
  : msg_(msg)
  {}
  Init_InterPol2_Request_p r(::my_robot_interfaces::srv::InterPol2_Request::_r_type arg)
  {
    msg_.r = std::move(arg);
    return Init_InterPol2_Request_p(msg_);
  }

private:
  ::my_robot_interfaces::srv::InterPol2_Request msg_;
};

class Init_InterPol2_Request_posz
{
public:
  explicit Init_InterPol2_Request_posz(::my_robot_interfaces::srv::InterPol2_Request & msg)
  : msg_(msg)
  {}
  Init_InterPol2_Request_r posz(::my_robot_interfaces::srv::InterPol2_Request::_posz_type arg)
  {
    msg_.posz = std::move(arg);
    return Init_InterPol2_Request_r(msg_);
  }

private:
  ::my_robot_interfaces::srv::InterPol2_Request msg_;
};

class Init_InterPol2_Request_posy
{
public:
  explicit Init_InterPol2_Request_posy(::my_robot_interfaces::srv::InterPol2_Request & msg)
  : msg_(msg)
  {}
  Init_InterPol2_Request_posz posy(::my_robot_interfaces::srv::InterPol2_Request::_posy_type arg)
  {
    msg_.posy = std::move(arg);
    return Init_InterPol2_Request_posz(msg_);
  }

private:
  ::my_robot_interfaces::srv::InterPol2_Request msg_;
};

class Init_InterPol2_Request_posx
{
public:
  Init_InterPol2_Request_posx()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_InterPol2_Request_posy posx(::my_robot_interfaces::srv::InterPol2_Request::_posx_type arg)
  {
    msg_.posx = std::move(arg);
    return Init_InterPol2_Request_posy(msg_);
  }

private:
  ::my_robot_interfaces::srv::InterPol2_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_robot_interfaces::srv::InterPol2_Request>()
{
  return my_robot_interfaces::srv::builder::Init_InterPol2_Request_posx();
}

}  // namespace my_robot_interfaces


namespace my_robot_interfaces
{

namespace srv
{

namespace builder
{

class Init_InterPol2_Response_description
{
public:
  explicit Init_InterPol2_Response_description(::my_robot_interfaces::srv::InterPol2_Response & msg)
  : msg_(msg)
  {}
  ::my_robot_interfaces::srv::InterPol2_Response description(::my_robot_interfaces::srv::InterPol2_Response::_description_type arg)
  {
    msg_.description = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_robot_interfaces::srv::InterPol2_Response msg_;
};

class Init_InterPol2_Response_success
{
public:
  Init_InterPol2_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_InterPol2_Response_description success(::my_robot_interfaces::srv::InterPol2_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return Init_InterPol2_Response_description(msg_);
  }

private:
  ::my_robot_interfaces::srv::InterPol2_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_robot_interfaces::srv::InterPol2_Response>()
{
  return my_robot_interfaces::srv::builder::Init_InterPol2_Response_success();
}

}  // namespace my_robot_interfaces

#endif  // MY_ROBOT_INTERFACES__SRV__DETAIL__INTER_POL2__BUILDER_HPP_

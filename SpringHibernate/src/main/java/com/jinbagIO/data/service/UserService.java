package com.jinbagIO.data.service;

import com.jinbagIO.data.model.User;

import java.util.List;

public interface UserService {
    void add(User user);
    List<User> listUsers();
    User findById(Long id);
    void deleteUserById(Long id);


}

package com.jinbagIO.data.dao;

import com.jinbagIO.data.model.User;

import java.util.List;

public interface UserDao {
    void add(User user);
    List<User> listUsers();
    User findById(Long id);
    void deleteUserById(Long id);
}

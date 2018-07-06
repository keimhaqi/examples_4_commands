package com.jinbagIO.data.daoImpl;

import com.jinbagIO.data.dao.AbstractDao;
import com.jinbagIO.data.dao.UserDao;
import com.jinbagIO.data.model.User;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
import javax.persistence.TypedQuery;
import javax.persistence.criteria.CriteriaQuery;
import javax.persistence.criteria.Root;
import java.util.List;

@Repository
public class UserDaoImpl extends AbstractDao<Integer, User> implements UserDao {
    /*
     *
     *
     * @author JOKA
     * @date 2018/5/1 23:24
     * @param
     * @return
     * JPA使用方法
     */
    /*
    @PersistenceContext
    private EntityManager entityManager;

    @Override
    public void add(User user) {
        entityManager.persist(user);
    }

    @Override
    public List<User> listUsers() {
        CriteriaQuery<User> criteriaQuery = entityManager.getCriteriaBuilder().createQuery(User.class);
        @SuppressWarnings("unused")
        Root<User> root = criteriaQuery.from(User.class);
        return entityManager.createQuery(criteriaQuery).getResultList();

    }
    */



    @Override
    public void add(User user) {
        persist(user);
    }

    @Override
    public List<User> listUsers() {
        CriteriaQuery<User> criteriaQuery = createEntityCriteria();
        @SuppressWarnings("unused")
        Root<User> root = criteriaQuery.from(User.class);
        return getSession().createQuery(criteriaQuery).getResultList();
    }

    @Override
    public User findById(Long id) {
        TypedQuery<User> query = getSession().createQuery("from User u where u.id=:id")
                .setParameter("id", id);
        return query.getSingleResult();
    }

    @Override
    public void deleteUserById(Long id) {
        User user = new User();
        user.setId(id);
        delete(user);
    }
}

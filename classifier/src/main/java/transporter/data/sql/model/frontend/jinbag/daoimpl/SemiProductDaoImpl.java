package transporter.data.sql.model.frontend.jinbag.daoimpl;

import transporter.data.sql.hibernateCfg.AbstractDao;
import transporter.data.sql.model.frontend.jinbag.dao.ISemiProductDao;
import transporter.data.sql.model.frontend.jinbag.entities.SemiProduct;
import org.springframework.stereotype.Repository;

import javax.persistence.TypedQuery;
import java.util.List;

@Repository
public class SemiProductDaoImpl extends AbstractDao<Long, SemiProduct> implements ISemiProductDao{
    @Override
    public List<SemiProduct> queryById(Long id) {
        TypedQuery<SemiProduct> query = getSession().createQuery("From SemiProduct sp where sp.id=:id")
                .setParameter("id", id);
        return query.getResultList();
    }
}

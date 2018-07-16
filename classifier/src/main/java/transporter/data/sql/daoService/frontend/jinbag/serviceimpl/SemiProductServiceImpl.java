package transporter.data.sql.daoService.frontend.jinbag.serviceimpl;

import transporter.data.sql.daoService.frontend.jinbag.services.ISemiProductService;
import transporter.data.sql.model.frontend.jinbag.dao.ISemiProductDao;
import transporter.data.sql.model.frontend.jinbag.entities.SemiProduct;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Configuration;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Configuration
public class SemiProductServiceImpl implements ISemiProductService{
    @Autowired
    private ISemiProductDao semiProductDao;
    @Transactional
    @Override
    public List<SemiProduct> queryById(Long id) {
        return semiProductDao.queryById(id);
    }
}

package transporter.data.sql.model.frontend.jinbag.dao;

import transporter.data.sql.model.frontend.jinbag.entities.SemiProduct;

import java.util.List;

public interface ISemiProductDao {
    List<SemiProduct> queryById(Long id);
}

package transporter.data.sql.model.frontend.jinbag.entities;

import javax.persistence.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "semi_product")
public class SemiProduct {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id", columnDefinition = "bigint(11)")
    private Long id;

    @Column(name = "product_id", columnDefinition = "bigint(11)")
    private Long productId;

    @Column(name = "in_product", columnDefinition = "tinyint(1)")
    private Integer inProduct;

    @Column(name = "beginning_time", columnDefinition = "timestamp")
    private LocalDateTime beginningTime;

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public Long getProductId() {
        return productId;
    }

    public void setProductId(Long productId) {
        this.productId = productId;
    }

    public Integer getInProduct() {
        return inProduct;
    }

    public void setInProduct(Integer inProduct) {
        this.inProduct = inProduct;
    }

    public LocalDateTime getBeginningTime() {
        return beginningTime;
    }

    public void setBeginningTime(LocalDateTime beginningTime) {
        this.beginningTime = beginningTime;
    }

    @Override
    public String toString() {
        return "SemiProduct{" +
                "id=" + id +
                ", productId=" + productId +
                ", inProduct=" + inProduct +
                ", beginningTime=" + beginningTime +
                '}';
    }
}

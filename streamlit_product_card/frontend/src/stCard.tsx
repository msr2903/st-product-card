import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib";
import React, { ReactNode } from "react";
import styled from "@emotion/styled";

type PicturePosition = "top" | "bottom" | "left" | "right";

interface ProductCardProps {
  args: {
    productName: string;
    description?: string[];
    price?: string;
    productImage?: string;
    buttonText?: string;
    useButton: boolean;
    picturePosition: PicturePosition;
    picturePaddings: boolean;
    enableAnimation: boolean;
    styles: {
      card?: React.CSSProperties;
      title?: React.CSSProperties;
      text?: React.CSSProperties;
      price?: React.CSSProperties;
      button?: React.CSSProperties;
      image?: React.CSSProperties;
    };
  };
  theme?: {
    font?: string;
    secondaryBackgroundColor?: string;
    textColor?: string;
    primaryColor?: string;
  };
}

class ProductCardComponent extends StreamlitComponentBase<ProductCardProps> {
  componentDidMount(): void {
    Streamlit.setComponentReady();
    Streamlit.setFrameHeight();
  }

  componentDidUpdate(): void {
    Streamlit.setFrameHeight();
  }

  private onCardClick = (): void => {
    Streamlit.setComponentValue({ buttonClicked: true });
  };

  private onButtonClick = (
    e: React.MouseEvent<HTMLButtonElement>
  ): void => {
    e.stopPropagation();
    Streamlit.setComponentValue({ buttonClicked: true });
  };

  render(): ReactNode {
    const { args, theme } = this.props;
    if (!theme) {
      return (
        <div style={{ color: "red", padding: 10 }}>
          ⚠️ Streamlit theme not found — upgrade to Streamlit 1.10+.
        </div>
      );
    }

    const {
      productName,
      description = [],
      price,
      productImage,
      buttonText = "Add to Cart",
      useButton,
      picturePosition,
      picturePaddings,
      enableAnimation,
      styles,
    } = args;

    const isHorizontal =
      picturePosition === "left" || picturePosition === "right";
    const flexDirection = isHorizontal ? "row" : "column";

    // 1) Compute the card's borderRadius (string)
    const defaultRadius = 12;
    // no optional chaining—fall back safely
    const rawBorder = styles.card && styles.card.borderRadius;
    const slotRadius =
      typeof rawBorder === "string" || typeof rawBorder === "number"
        ? rawBorder
        : undefined;
    const cardRadius =
      typeof slotRadius === "string"
        ? slotRadius
        : typeof slotRadius === "number"
        ? `${slotRadius}px`
        : `${defaultRadius}px`;

    // 2) Card container
    const Card = styled.div({
      display: "flex",
      flexDirection,
      fontFamily: `${theme.font}, sans-serif`,
      backgroundColor: theme.secondaryBackgroundColor,
      borderRadius: cardRadius,
      boxShadow: "0 6px 20px rgba(0,0,0,0.12)",
      overflow: "hidden",
      maxWidth: isHorizontal ? 500 : 320,
      margin: "auto",
      position: "relative",
      cursor: useButton ? "default" : "pointer",
      ...(enableAnimation && {
        transform: "scale(0.95)",
        transition: "transform 0.2s ease-in-out",
        "&:hover": { transform: "scale(1)" },
        "&:active": { transform: "scale(0.95)" },
      }),
      ...styles.card,
    });

    // 3) Image styling with matching radius when padded
    const Image = styled.img({
      width: isHorizontal ? 180 : "100%",
      height: isHorizontal ? "auto" : 180,
      objectFit: "cover",
      borderRadius: picturePaddings
        ? cardRadius
        : isHorizontal
        ? picturePosition === "left"
          ? `${cardRadius} 0 0 ${cardRadius}`
          : `0 ${cardRadius} ${cardRadius} 0`
        : picturePosition === "top"
        ? `${cardRadius} ${cardRadius} 0 0`
        : `0 0 ${cardRadius} ${cardRadius}`,
      marginLeft:
        isHorizontal && picturePosition === "right" ? 12 : 0,
      marginRight:
        isHorizontal && picturePosition === "left" ? 12 : 0,
      marginTop:
        !isHorizontal && picturePosition === "bottom" ? 12 : 0,
      marginBottom:
        !isHorizontal && picturePosition === "top" ? 12 : 0,
      ...(picturePaddings
        ? { padding: 12, boxSizing: "border-box" }
        : {}),
      ...styles.image,
    });

    // 4) Content
    const Content = styled.div({
      flex: 1,
      padding: 20,
      display: "flex",
      flexDirection: "column",
      justifyContent: "space-between",
      ...styles.card,
    });

    const Title = styled.h3({
      margin: 0,
      fontSize: "1.1rem",
      color: theme.textColor,
      ...styles.title,
    });

    const Text = styled.div({
      fontSize: "0.85rem",
      color: theme.textColor,
      margin: "8px 0 12px",
      lineHeight: 1.4,
      ...styles.text,
    });

    const PriceTag = styled.div({
      fontSize: "1.3rem",
      fontWeight: 600,
      color: theme.primaryColor,
      ...styles.price,
    });

    const Button = styled.button({
      backgroundColor: theme.primaryColor,
      color: "#fff",
      border: "none",
      padding: "10px 16px",
      borderRadius: 6,
      cursor: "pointer",
      fontSize: "0.9rem",
      alignSelf: isHorizontal ? "flex-start" : "center",
      ...styles.button,
    });

    const descContent: ReactNode[] = description.map(
      (line: string, i: number) => (
        <span key={i}>
          {line}
          <br />
        </span>
      )
    );

    return (
      <Card onClick={!useButton ? this.onCardClick : undefined}>
        {(picturePosition === "top" ||
          picturePosition === "left") &&
          productImage && <Image src={productImage} alt={productName} />}

        <Content>
          <Title>{productName}</Title>
          {description.length > 0 && <Text>{descContent}</Text>}
          {price && <PriceTag>{price}</PriceTag>}
          {useButton && (
            <Button onClick={this.onButtonClick}>{buttonText}</Button>
          )}
        </Content>

        {(picturePosition === "bottom" ||
          picturePosition === "right") &&
          productImage && <Image src={productImage} alt={productName} />}
      </Card>
    );
  }
}

export default withStreamlitConnection(ProductCardComponent);
import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib";
import React, { ReactNode } from "react";
import styled from "@emotion/styled";
import { Global, css } from '@emotion/react'; 
import * as CSS from 'csstype'; 

const kebabToCamel = (str: string): string => {
  return str.replace(/-([a-z0-9])/g, (match, char) => char.toUpperCase());
};

const transformKebabCaseStyles = (styleObj?: { [key: string]: any }): React.CSSProperties => {
  if (!styleObj) return {};
  const newStyles: { [key: string]: any } = {}; 
  for (const key in styleObj) {
    if (Object.prototype.hasOwnProperty.call(styleObj, key)) {
      newStyles[kebabToCamel(key)] = styleObj[key];
    }
  }
  return newStyles as React.CSSProperties; 
};

type PicturePosition = "top" | "bottom" | "left" | "right";
type MobileBreakpointBehavior = "stack top" | "stack bottom" | "shrink" | "none";
type EmotionCompatibleStyle = { [key: string]: any };

interface ProductCardArgs {
  productName: string;
  description?: string[];
  price?: string;
  productImage?: string;
  buttonText: string; 
  picturePosition: PicturePosition;
  enableAnimation: boolean;
  imageWidthPercent: number;
  imageAspectRatio: string; 
  imageObjectFit: CSS.Property.ObjectFit; 
  mobileBreakpointBehavior: MobileBreakpointBehavior;
  fontUrl?: string;
  styles: { 
    card?: EmotionCompatibleStyle; 
    title?: EmotionCompatibleStyle;
    text?: EmotionCompatibleStyle;
    price?: EmotionCompatibleStyle;
    button?: EmotionCompatibleStyle;
    image?: EmotionCompatibleStyle; 
  };
}

interface ProductCardProps {
  args: ProductCardArgs;
  theme?: {
    font?: string;
    secondaryBackgroundColor?: string;
    textColor?: string;
    primaryColor?: string;
  };
}

const globalStyles = css`
  body {
    margin: 0; 
    padding: 10px; 
    box-sizing: border-box;
  }
  #root { 
    width: 100%;
    height: 100%;
  }
`;

class ProductCardComponent extends StreamlitComponentBase<ProductCardProps> {
  componentDidMount(): void {
    Streamlit.setComponentReady();
    Streamlit.setFrameHeight();
  }

  componentDidUpdate(): void {
    Streamlit.setFrameHeight();
  }

  private sendClickEvent = (): void => {
    Streamlit.setComponentValue({ clickEventId: Date.now() });
  }

  private onCardClick = (): void => {
    if (!this.props.args.buttonText || this.props.args.buttonText.trim() === "") {
        this.sendClickEvent();
    }
  };

  private onButtonClick = (
    e: React.MouseEvent<HTMLButtonElement>
  ): void => {
    e.stopPropagation(); 
    this.sendClickEvent();
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
      buttonText, 
      picturePosition,
      enableAnimation,
      styles, 
      fontUrl,
      imageWidthPercent,
      imageAspectRatio,
      imageObjectFit,
      mobileBreakpointBehavior,
    } = args;

    // Transform kebab-case keys from Python styles to camelCase for React/Emotion
    const userCardStyles = transformKebabCaseStyles(styles.card);
    const userImageStyles = transformKebabCaseStyles(styles.image);
    const userTextStyles = transformKebabCaseStyles(styles.text);
    const userTitleStyles = transformKebabCaseStyles(styles.title);
    const userPriceStyles = transformKebabCaseStyles(styles.price);
    const userButtonStyles = transformKebabCaseStyles(styles.button);

    const isHorizontalLayout =
      picturePosition === "left" || picturePosition === "right";
    
    const showButton = buttonText && buttonText.trim() !== "";

    const defaultRadius = 12;
    const rawBorderRadius = userCardStyles.borderRadius; 
    const cardRadius =
      typeof rawBorderRadius === "string"
        ? rawBorderRadius
        : typeof rawBorderRadius === "number"
        ? `${rawBorderRadius}px`
        : `${defaultRadius}px`;

    // Define styled components by merging defaults and user styles into a single object
    const Title = styled.h3({ 
      margin: 0,
      fontSize: "clamp(0.9rem, 0.5vw + 0.8rem, 1.2rem)",
      color: theme.textColor, 
      fontWeight: 600,
      ...userTitleStyles, // User styles spread last to override defaults
    });

    const Text = styled.div({
      fontSize: "clamp(0.8rem, 0.4vw + 0.7rem, 1rem)",
      color: theme.textColor,
      margin: "8px 0 12px",
      lineHeight: 1.5,
      ...userTextStyles,
    });

    const PriceTag = styled.div({
      fontSize: "clamp(1rem, 0.6vw + 0.8rem, 1.5rem)",
      fontWeight: 600,
      color: theme.primaryColor,
      ...userPriceStyles,
    });

    const Button = styled.button({
      backgroundColor: theme.primaryColor,
      color: "#fff",
      border: "none",
      padding: "10px 16px",
      borderRadius: 6,
      cursor: "pointer",
      fontSize: "clamp(0.8rem, 0.5vw + 0.7rem, 1rem)",
      alignSelf: isHorizontalLayout ? "flex-start" : "center",
      marginTop: "auto",
      ...userButtonStyles,
    });

    const descContent: ReactNode[] = description.map(
      (line: string, i: number) => (
        <span key={i}>
          {line}
          {i < description.length -1 && <br />}
        </span>
      )
    );
    
    return (
      <>
        <Global styles={globalStyles} /> 
        {fontUrl && (
          <style dangerouslySetInnerHTML={{ __html: `@import url('${fontUrl}');` }} />
        )}
        <StyledCard
          userCardStyleProps={userCardStyles} 
          isHorizontalProp={isHorizontalLayout}
          cardBorderRadiusProp={cardRadius}
          enableAnimationProp={enableAnimation}
          themeFont={theme.font}
          themeSecondaryBackgroundColor={theme.secondaryBackgroundColor}
          onClick={this.onCardClick} 
          picturePositionProp={picturePosition} 
          mobileBreakpointBehaviorProp={mobileBreakpointBehavior}
          hasButton={showButton} 
        >
          {(picturePosition === "top" || picturePosition === "left") && productImage && (
              <StyledImageContainer
                isHorizontalProp={isHorizontalLayout}
                imageWidthPercentProp={imageWidthPercent}
                picturePositionProp={picturePosition}
                mobileBreakpointBehaviorProp={mobileBreakpointBehavior}
                imageAspectRatioProp={imageAspectRatio} 
                cardBorderRadiusProp={cardRadius} 
              >
                <ImgComponent
                  src={productImage}
                  alt={productName}
                  userImageStyleProps={userImageStyles} 
                  imageAspectRatioProp={imageAspectRatio} 
                  imageObjectFitProp={imageObjectFit}
                />
              </StyledImageContainer>
            )}

          <StyledContent
            isHorizontalProp={isHorizontalLayout}
            userContentStyleProps={userTextStyles} 
            mobileBreakpointBehaviorProp={mobileBreakpointBehavior}
            picturePositionProp={picturePosition} 
          >
            <Title>{productName}</Title>
            {description.length > 0 && <Text>{descContent}</Text>}
            {price && <PriceTag>{price}</PriceTag>}
            {showButton && ( 
              <Button onClick={this.onButtonClick}>{buttonText}</Button>
            )}
          </StyledContent>

          {(picturePosition === "bottom" || picturePosition === "right") && productImage && (
               <StyledImageContainer
                isHorizontalProp={isHorizontalLayout}
                imageWidthPercentProp={imageWidthPercent}
                picturePositionProp={picturePosition}
                mobileBreakpointBehaviorProp={mobileBreakpointBehavior}
                imageAspectRatioProp={imageAspectRatio}
                cardBorderRadiusProp={cardRadius} 
              >
                <ImgComponent
                  src={productImage}
                  alt={productName}
                  userImageStyleProps={userImageStyles} 
                  imageAspectRatioProp={imageAspectRatio}
                  imageObjectFitProp={imageObjectFit}
                />
              </StyledImageContainer>
            )}
        </StyledCard>
      </>
    );
  }
}

interface StyledCardProps {
  userCardStyleProps: React.CSSProperties; 
  isHorizontalProp: boolean;
  cardBorderRadiusProp: string;
  enableAnimationProp: boolean;
  themeFont?: string;
  themeSecondaryBackgroundColor?: string;
  onClick?: (event: React.MouseEvent<HTMLDivElement, MouseEvent>) => void;
  picturePositionProp: PicturePosition; 
  mobileBreakpointBehaviorProp: MobileBreakpointBehavior; 
  hasButton: boolean; 
}

interface StyledImageContainerProps {
  isHorizontalProp: boolean;
  imageWidthPercentProp: number;
  picturePositionProp: PicturePosition;
  mobileBreakpointBehaviorProp: MobileBreakpointBehavior; 
  imageAspectRatioProp: string; 
  cardBorderRadiusProp: string; 
}

interface ImgComponentProps {
  userImageStyleProps: React.CSSProperties; 
  imageAspectRatioProp: string;
  imageObjectFitProp: CSS.Property.ObjectFit; 
}

interface StyledContentProps {
  isHorizontalProp: boolean;
  userContentStyleProps: React.CSSProperties; 
  mobileBreakpointBehaviorProp: MobileBreakpointBehavior; 
  picturePositionProp: PicturePosition;
}

const ImgComponent = styled.img<ImgComponentProps>(props => {
  let imageSpecificAspectRatio: CSS.Property.AspectRatio;
  switch (props.imageAspectRatioProp) {
    case "native":
      imageSpecificAspectRatio = "auto";
      break;
    default:
      imageSpecificAspectRatio = props.imageAspectRatioProp === "1/1" ? "1 / 1" : props.imageAspectRatioProp;
  }

  const baseImageStyles: React.CSSProperties = {
    display: "block",
    width: "100%", 
    height: imageSpecificAspectRatio === "auto" && props.imageAspectRatioProp === "native" ? "auto" : "100%",
    objectFit: props.userImageStyleProps.objectFit || props.imageObjectFitProp,
  };
  if (props.imageAspectRatioProp === "native") { 
    baseImageStyles.aspectRatio = imageSpecificAspectRatio;
  }

  return {
    ...baseImageStyles,
    ...props.userImageStyleProps, 
    objectFit: props.userImageStyleProps.objectFit || props.imageObjectFitProp,
    ...( (props.imageAspectRatioProp === "native" && !props.userImageStyleProps.aspectRatio) && 
        { aspectRatio: imageSpecificAspectRatio } )
  };
});

const StyledImageContainer = styled.div<StyledImageContainerProps>(props => {
  const isCurrentlyHorizontal = props.isHorizontalProp &&
    !( (props.mobileBreakpointBehaviorProp === 'stack top' || props.mobileBreakpointBehaviorProp === 'stack bottom') && 
        typeof window !== 'undefined' && window.innerWidth <= 600);

  const baseStyles: CSS.Properties<string | number> & { [key: string]: any } = { 
    display: 'flex', 
    justifyContent: 'center',
    alignItems: 'center',
    overflow: 'hidden', 
    flexShrink: isCurrentlyHorizontal ? 0 : undefined, 
    width: isCurrentlyHorizontal ? `${props.imageWidthPercentProp}%` : "100%",
    marginLeft: isCurrentlyHorizontal && props.picturePositionProp === "right" ? "12px" : "0",
    marginRight: isCurrentlyHorizontal && props.picturePositionProp === "left" ? "12px" : "0",
    marginTop: !isCurrentlyHorizontal && props.picturePositionProp === "bottom" ? "12px" : "0",
    marginBottom: !isCurrentlyHorizontal && props.picturePositionProp === "top" ? "12px" : "0",
    borderRadius: props.isHorizontalProp
      ? props.picturePositionProp === "left"
        ? `${props.cardBorderRadiusProp} 0 0 ${props.cardBorderRadiusProp}`
        : `0 ${props.cardBorderRadiusProp} ${props.cardBorderRadiusProp} 0`
      : props.picturePositionProp === "top"
      ? `${props.cardBorderRadiusProp} ${props.cardBorderRadiusProp} 0 0`
      : `0 0 ${props.cardBorderRadiusProp} ${props.cardBorderRadiusProp}`,
  };
  
  const propAspectRatio = props.imageAspectRatioProp;
  if (propAspectRatio !== "native") { 
      baseStyles.aspectRatio = propAspectRatio === "1/1" ? "1 / 1" : propAspectRatio;
  }

  let responsiveStyles = {};
  if (props.isHorizontalProp && (props.mobileBreakpointBehaviorProp === 'stack top' || props.mobileBreakpointBehaviorProp === 'stack bottom')) {
    const mobileSpecificStyles: CSS.Properties<string | number> = {
        width: "100%", 
        flexBasis: "auto", 
        flexShrink: undefined,
        marginLeft: "0",
        marginRight: "0",
        marginTop: "0", 
        marginBottom: "0",
        borderRadius: props.mobileBreakpointBehaviorProp === 'stack top' 
            ? `${props.cardBorderRadiusProp} ${props.cardBorderRadiusProp} 0 0` 
            : `0 0 ${props.cardBorderRadiusProp} ${props.cardBorderRadiusProp}`,
    };
    if (props.mobileBreakpointBehaviorProp === 'stack top') { 
        mobileSpecificStyles.marginBottom = "12px";
    } else { 
        mobileSpecificStyles.marginTop = "12px";
    }
    responsiveStyles = {
        "@media (max-width: 600px)": mobileSpecificStyles
    };
  }
  return {
    ...baseStyles,
    ...responsiveStyles, 
  };
});

const StyledCard = styled.div<StyledCardProps>(props => {
  const baseStyles: React.CSSProperties = {
    display: "flex",
    width: "100%", 
    height: "auto",
    fontFamily: `${props.themeFont}, sans-serif`,
    backgroundColor: props.themeSecondaryBackgroundColor,
    borderRadius: props.cardBorderRadiusProp,
    boxShadow: "0 6px 20px rgba(0,0,0,0.08)", 
    overflow: "hidden", 
    position: "relative",
    cursor: props.hasButton ? "default" : (props.onClick ? "pointer" : "default"),
    flexDirection: props.isHorizontalProp ? "row" : "column",
  };

  const conditionalStyles: { [key: string]: any } = {}; 

  if (props.enableAnimationProp) {
    conditionalStyles.willChange = "transform, box-shadow"; 
    conditionalStyles.transition = "transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out"; 
    conditionalStyles["&:hover"] = { 
      transform: "scale(1.03)",
      boxShadow: "0 8px 25px rgba(0,0,0,0.12)",
    };
    conditionalStyles["&:active"] = { 
      transform: "scale(0.98)",
    };
  }
  
  if (props.isHorizontalProp) { 
    let mobileFlexDirection: CSS.Property.FlexDirection = "column"; 

    if (props.mobileBreakpointBehaviorProp === "stack top") {
        mobileFlexDirection = props.picturePositionProp === "right" ? "column-reverse" : "column";
    } else if (props.mobileBreakpointBehaviorProp === "stack bottom") {
        mobileFlexDirection = props.picturePositionProp === "left" ? "column-reverse" : "column";
    }
     if (props.mobileBreakpointBehaviorProp === "stack top" || props.mobileBreakpointBehaviorProp === "stack bottom") {
        conditionalStyles["@media (max-width: 600px)"] = {
          ...(conditionalStyles["@media (max-width: 600px)"] as object), 
          flexDirection: mobileFlexDirection, 
        };
     }
  }
  
  return {
    ...baseStyles,
    ...conditionalStyles,
    ...props.userCardStyleProps, 
  };
});

const StyledContent = styled.div<StyledContentProps>(props => {
  const baseStyles: React.CSSProperties = {
    display: "flex",
    flexDirection: "column",
    justifyContent: "center", 
    padding: "20px",
    minWidth: 0, 
    boxSizing: "border-box",
    flexGrow: props.isHorizontalProp ? 1 : undefined, 
    flexBasis: props.isHorizontalProp ? "0px" : "auto",  
    width: "100%", 
  };
  
  const responsiveStyles: { [key: string]: any } = {}; 
  if (props.isHorizontalProp && (props.mobileBreakpointBehaviorProp === 'stack top' || props.mobileBreakpointBehaviorProp === 'stack bottom')) {
     const mobileSpecificContentStyles: React.CSSProperties = {
        flexGrow: 0, 
        flexBasis: "auto",
        width: "100%", 
        padding: "20px", 
     };
     if (props.mobileBreakpointBehaviorProp === 'stack top'){ 
        mobileSpecificContentStyles.paddingTop = (props.picturePositionProp === "left" || props.picturePositionProp === "right") ? "0px" : "20px";
     }
     if (props.mobileBreakpointBehaviorProp === 'stack bottom'){ 
        mobileSpecificContentStyles.paddingBottom = (props.picturePositionProp === "left" || props.picturePositionProp === "right") ? "0px" : "20px";
     }
     responsiveStyles["@media (max-width: 600px)"] = mobileSpecificContentStyles;
  }

  return {
    ...baseStyles,
    ...responsiveStyles,
    ...props.userContentStyleProps, 
  };
});

export default withStreamlitConnection(ProductCardComponent);


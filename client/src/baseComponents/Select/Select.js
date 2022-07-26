import React, { useState } from 'react';
import cx from 'classnames';
import { Div, Select as BaseSelect } from 'basedesign-iswad';

import styles from './Select.module.scss';

const Select = ({
  val,
  setVal,
  selectIntialShownText,
  options,
  openOptionsDownWard,
  placeHolder
}) => {
  const [isOptionsActive, setIsOptionsActive] = useState(false);

  return (
    <>
      {isOptionsActive && (
        <Div
          className={cx(
            'w-per-100 height-vh-full bgWhite pos-fix pos-fix--lt op-10 z-100',
            styles.clickable
          )}
          onClick={() => setIsOptionsActive(false)}
        />
      )}
      <BaseSelect
        selectValue={val}
        setSelectValue={setVal}
        options={options}
        className={cx(styles.select)}
        defaultViewClassName={cx('w-per-100 pt1 pb1 pl2 pr2', styles.defaultSelect)}
        optionClassName={cx(styles.option)}
        optinsContainerClassName={cx(styles.optionsContainer)}
        searchContainerClassName="w-per-100"
        inputSearchClassName={cx(styles.searchInput)}
        placeHolderClassName={cx('fs-px-12', styles.placeHolder)}
        fullWidth
        arrowIconFillColor="gray"
        arrowIconStrokeColor="gray"
        arrowIconScale={0.8}
        searchIconFillColor="gray"
        searchIconStrokeColor="gray"
        openOptionsDownWard={openOptionsDownWard}
        isOptionsActive={isOptionsActive}
        setIsOptionsActive={setIsOptionsActive}
        selectIntialShownText={selectIntialShownText}
        placeHolder={placeHolder || 'Choose an option...'}
      />
    </>
  );
};

export default Select;
